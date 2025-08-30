import json
from pathlib import Path
from typing import Any, Union


class MyEncoder(json.JSONEncoder):
    """
    自定义 JSON 编码器，支持 datetime、bytes、numpy 类型的序列化。
    """

    def default(self, obj: Any) -> Any:
        import datetime

        try:
            import numpy as np
        except ImportError:
            np = None

        if isinstance(obj, datetime.datetime):
            # datetime 对象转字符串
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, bytes):
            # bytes 转字符串
            return obj.decode("utf-8")
        elif np is not None:
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
        # 其他类型使用父类默认方法
        return super().default(obj)


class Json:
    """
    JSON 文件读写与序列化工具类。
    """

    @staticmethod
    def load(file: str | Path):
        with open(file, "r", encoding="utf-8") as f:
            _data = json.load(f)
        return _data

    @staticmethod
    def save(
        data: Any, file: Union[str, Path], ensure_ascii: bool = False, indent: int = 4
    ) -> None:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii, cls=MyEncoder)

    @staticmethod
    def to_str(obj: Any, ensure_ascii: bool = False, indent: int = 4) -> str:
        # 支持的原生类型：
        # Python -> JSON
        # int, float: number
        # True: true
        # False: false
        # None: null
        # str: string
        # list,tuple: array
        # dict: object
        return json.dumps(obj, cls=MyEncoder, indent=indent, ensure_ascii=ensure_ascii)
