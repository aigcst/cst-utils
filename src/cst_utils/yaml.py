import re
from pathlib import Path

import yaml


class Yaml:
    @staticmethod
    def save(obj, file: str | Path, allow_unicode=True):
        with open(file, "w", encoding="utf-8") as f:
            yaml.dump(obj, f, allow_unicode=True)

    @staticmethod
    def load(file: str | Path = "data.yaml", append_filename=False) -> dict:
        assert Path(file).suffix in (".yaml", ".yml"), (
            f"尝试加载一个非 yaml 的文件: {file}"
        )
        with open(file, errors="ignore", encoding="utf-8") as f:
            s = f.read()  # string

            # 去除特殊字符
            if not s.isprintable():
                s = re.sub(
                    r"[^\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010ffff]+",
                    "",
                    s,
                )

            # 添加yaml文件名到返回的dict
            # 总是返回一个字典(yaml.safe_load() 在空文件时会返回None)
            data = yaml.safe_load(s) or {}
            if append_filename:
                data["yaml_file"] = str(file)
            return data


if __name__ == "__main__":
    _ = Yaml.load(Path(r"test.yaml"))
    print(_)
