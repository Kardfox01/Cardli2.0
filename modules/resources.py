import os


j = os.path.join

class Resources:
    __dir: str
    __type: str

    def __init__(self, dir: str, type: str=None) -> None:
        self.__dir = dir
        self.__type = type

        files = os.listdir(self.__dir)
        files = [file for file in files if os.path.isdir(j(self.__dir, file))]

        for dir in files:
            self.__setattr__(dir, Resources(j(self.__dir, dir), type=dir))

    def __getitem__(self, name: str):
        if self.__type:
            try:
                with open(j(self.__dir, name), "r") as file:
                    return file.read()
            except Exception: pass
        return None