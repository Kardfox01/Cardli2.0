import os


join = os.path.join

class Resources:
    __dir: str

    def __init__(self, dir: str) -> None:
        self.__dir = dir

        files = os.listdir(self.__dir)
        files = [file for file in files if os.path.isdir(join(self.__dir, file))]

        for dir in files:
            self.__dict__[dir] = Resources(join(self.__dir, dir))

    def __getitem__(self, name: str):
        try:
            with open(join(self.__dir, name), "r") as file:
                return file.read()
        except Exception:
            return join(self.__dir, name)