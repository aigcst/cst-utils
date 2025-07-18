from typing import Optional
from pathlib import Path
from git import Repo


class GitRepo:
    def __init__(self, local_path: Path, repo_url: Optional[str] = None, branch='master'):
        self.local_path = local_path
        self.repo_url = repo_url
        self.initial(repo_url, branch)

    def initial(self, repo_url, branch):
        '''初始化仓库'''
        self.local_path.mkdir(exist_ok=True)

        git_local_path = Path(self.local_path, '.git')
        if not git_local_path.exists():
            self.repo = Repo.clone_from(repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self, branch='origin'):
        '''从线上拉取最新代码'''
        return self.repo.git.pull('--progress', branch)

    def push(self):
        self.repo.remotes.origin.push()

    def active_branch(self):
        return self.repo.active_branch

    def reset(self):
        '''撤销未提交的更改'''
        self.repo.git.reset('--hard', 'HEAD')

    def delete_branch(self, branch_name):
        '''删除分支'''
        self.repo.delete_head(branch_name)

    def status(self):
        '''获取仓库的状态'''
        repo_status = self.repo.git.status()
        print(repo_status)

    def add(self):
        self.repo.git.add(all=True)

    def commit(self, commit_msg: str):
        self.repo.git.commit('-m', commit_msg)

    def create_branch(self, branch_name):
        self.repo.create_head(branch_name)

    @property
    def branches(self):
        '''获取所有分支'''
        branches = self.repo.remote().refs
        return [
            item.remote_head
            for item in branches
            if item.remote_head
            not in [
                'HEAD',
            ]
        ]

    @property
    def commits(self):
        '''获取所有提交记录'''
        commit_log = self.repo.git.log(
            '--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
            max_count=50,
            date='format:%Y-%m-%d %H:%M',
        )
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    @property
    def tags(self):
        '''获取所有tag'''
        return [tag.name for tag in self.repo.tags]

    def change_to_branch(self, branch):
        '''切换分支'''
        return self.repo.git.checkout(branch)

    def change_to_commit(self, branch, commit):
        '''切换 commit：回滚'''
        self.change_to_branch(branch=branch)
        return self.repo.git.reset('--hard', commit)

    def change_to_tag(self, tag):
        '''切换tag'''
        return self.repo.git.checkout(tag)
