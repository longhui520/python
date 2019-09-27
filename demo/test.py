# 魔术方法 __str__ 和 __repr__
class Student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object %s' % self.name
    __repr__ = __str__     

# print(Student('Michal'))  
# 实现迭代功能的类
class Fib(object):
    def __init__(self,max):
        self.a,self.b,self.count,self.max = 0,1,0,max

    def __iter__(self):
        return self

    def __next__:
        if(self.count>=self.max){
            raise StopIteration
        }
        self.a,self.b = self.b,self.a+self.b
        self.count += 1
        return self.a
                     