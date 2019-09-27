from types import MethodType
class Student(object):
    __slots__ = ('name','set_age','age')
    pass
s = Student()
s.name = 'Michel'
print(s.name)    
def set_age(self,age):
    self.age = age

s.set_age = MethodType(set_age,s)
s.set_age(25)