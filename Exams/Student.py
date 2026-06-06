class Student:
    def __init__(self, id: str = "", name: str = "", score: int = 0.0) -> None:
        self.__id, self.__name, self.__score = id, name, score
    
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        self.__id = id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int) -> None:
        self.__score = score

    def getGrade(self) -> str:
        score_grade = {80: "A", 75: "B+", 70: "B", 65: "C+", 60: "C", 55: "D+", 50: "D", 0: "F"}
        for s in score_grade:
            if self.__score >= s: return score_grade[s]
    
    def toString(self) -> str:
        return f"{self.__id, self.__name, self.__score}"
    
    def toGrade(self):
        return f"{self.toString(), self.getGrade()}"

