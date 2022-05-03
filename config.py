import os
from copy import deepcopy
from functools import wraps

from yaml import FullLoader, load


def Singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@Singleton
class Configuration:

    def __init__(self) -> None:
        with open('./config.yml', mode="r", encoding="utf-8") as f:
            self.__config = load(f, Loader=FullLoader)
        if (os.path.exists("./config_custom.yml")):
            with open('./config_custom.yml', mode="r", encoding="utf-8") as f:
                customConfig = load(f, Loader=FullLoader)
                self.__config = self.__deepMerge(self.__config, customConfig)
        self.__cache = {}

    def __deepMerge(self, a, b, path=None):
        if path is None:
            path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self.__deepMerge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass
                else:
                    a[key] = b[key]
            else:
                a[key] = b[key]
        return a

    def setProperty(self, key: str, value: any) -> None:
        config = self.__config
        try:
            segments = key.split(".")
            for segment in segments:
                if (not isinstance(config[segment], dict)):
                    config[segment] = value
                config = config[segment]
        except KeyError:
            print(f"wrong property key:{key}")
        else:
            print(f"set property:{key}={config}")
            self.__cache[key] = config
        pass

    def getProperty(self, key: str) -> None:
        if (key in self.__cache):
            print(f"read property:{key}={self.__cache[key]}")
            return self.__cache[key]
        config = deepcopy(self.__config)
        try:
            for segment in key.split("."):
                config = config[segment]
        except KeyError:
            print(f"wrong property key:{key}")
        else:
            print(f"read property:{key}={config}")
            self.__cache[key] = config
        return config
