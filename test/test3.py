# 九九乘法表
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(row * col, end=" ")
#     print("")


def printline(row):
    for col in range(1, row + 1):
        print(row * col, end=" ")
    print("")


for row in range(1, 10):
    printline(row)


# 报名
def reg(name, age, sex='male'):
    if sex == 'male':
        print('{0} is {1},and he is a good student'.format(name, age))
    else:
        print('{0} is {1},and she is a good student'.format(name, age))


reg("liming", 21)
reg('lily', 23, 'female')


# 函数 touple 普通参数
def stu(*args):
    print("hello,大家好，我简单自我介绍一下：")
    print(type(args))
    for i in args:
        print(i)


stu('ff', 21, "man")
stu('enen')


# 函数 dict 关键字参数
def stt(**kwargs):
    print("hello,大家好：")
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, "---", v)


stt(name="jj", age=45, pro='eeeeee')
print("*" * 30)


# 混合函数
def mix(name, age, *args, hobby="唱歌", **kwargs):
    print("-" * 20)
    print("我是{0},今年{1}岁".format(name, age))
    if hobby == '唱歌':
        print("我的爱好是{0}".format(hobby))
    else:
        print("I don't have hobby")
    for i in args:
        print(i)
    print("-" * 30)
    for k, v in kwargs.items():
        print(k, "----", v)


# 开始调用函数
name = 'lili'
age = 23
mix(name, age)
mix(name, age, hobby='跳舞')
mix(name, age, 'wang', "yang", hobby='跳舞', hobby2="yinyue")


# 函数的返回值
def fun1():
    print("有返回值")
    return 1


def fun2():
    print("没有返回值")


f1 = fun1()
print(f1)
f2 = fun2()
print(f2)


# 函数文档
def ss(name, *args):
    '''
    第一行啊
    第二行行啊
    第三行行行啊
    '''




help(ss)
print("*" * 30)
print(ss.__doc__)
