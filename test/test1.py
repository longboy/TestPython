'''
简单函数：
1 写一个函数代码，返回这3个数字中最大的一个。

a = 123

b = 345

c = 444

'''


def max_num(*args):
    return max(args)


print(max_num(123, 345, 444))


def max_num1(*args):
    l = []
    for i in args:
        l.append(i)
    l.sort()
    return l[-1]


print(max_num1(123, 345, 444))
'''
2 分别写2个函数，完成下面的功能：

提示一下用到函数的：**和*，猩猩是字典，星是元组

2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果： 
 
[22, 44, 88]

2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：

('xaay','yaay','zaay')
'''


def ainfo(**kwargs):
    l = []
    for v in kwargs.values():
        l.append(v)
        l.sort()
    return l


print(ainfo(x=88, y=22, z=44))


def cinfo(**kwargs):
    l = []
    for k in kwargs.keys():
        l.append('%saay' % k)
    return tuple(l)


print(cinfo(x=88, y=22, z=44))