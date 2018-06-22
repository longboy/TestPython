class Animal():
    name = 'animal'

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("sleeppppppp")

    def jiao(self):
        print("emmmmmmm")


class mao(Animal):
    def __init__(self, name):
        self.name = name

    def jiao(self):
        print('%s jiaojiao' % self.name)


class dog(Animal):
    def __init__(self, name):
        self.name = name

    def yao(self):
        print('yaoyaoyao')


n = mao("mm")
n.jiao()


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.score, lisa.get_grade())
print(bart.name, bart.score, bart.get_grade())
