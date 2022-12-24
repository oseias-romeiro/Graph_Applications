
class Element:

    def __init__(self, value: int) -> None:
        self.__value: int = value
        self.__covered: int = 0

    def setValue(self, value: int) -> None:
        self.__value = value

    def getValue(self) -> int:
        return self.__value
    
    def get_covered(self) -> int:
        return self.__covered

    def set_cover(self):
        self.__covered += 1
    
    def isCovered(self):
        return self.__covered > 0

