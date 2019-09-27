class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be a interger')
        if value < 0 or value >100:
            raise ValueError('score must be 0 ~ 100')
        self.__score = value

s = Student()
s.score = 550
print(s.score)

