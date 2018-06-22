# oop基础
class Student():
    name = 'lili'
    age = 18


Student.__dict__
# 创建实例
yy = Student()
yy.__dict__
print(yy.name)


class A():
    name = 'yj'
    age = 21

    def say(self):
        self.name = 'aaa'
        self.age = 23


print(A.name)
print(A.age)
print("*" * 20)
print(id(A.name))
print(id(A.age))
print("*" * 20)
a = A()
# 查看A的属性
print(A.__dict__)
print(a.__dict__)
a.name='nn'
a.age='1'
print("---"*5)
print(a.__dict__)
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
