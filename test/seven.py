'''
一: 已知：元组 a = (1,2,3) 利用list方法，输出下面的结果：

(1,2,4)
'''
print('第一题：')
a = (1, 2, 3)
b = list(a)
b[-1] = 4
a = tuple(b)
print(a)
'''
二: 利用列表推导完成下面习题：

1 输出结果：[1 love python,2 love python,3 love python,.... 10 love python]

2 输出结果：[(0,0),(0,2),(2,0),(2,2)
'''
print('第二题：')
print(['%s love python' % s for s in range(1, 11)])
print(['{} love python'.format(i) for i in range(1, 11)])

print([(x, y) for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0])

'''
三：

a = [1,2,3]
b = a[:]
del a

b的值是什么。为什么呢？
'''
a = [1, 2, 3]
b = a[:]
del a
print(b)

'''
一 元组；a = (1,2,3)

1 有2种方法输出实现下面的结果：

(5,2,3)


2 判断2是否在元组里

'''
print('第一题：')
# 第一种：
a = (1, 2, 3)
b = list(a)
b[0] = 5
a = tuple(b)
print(a)

print(2 in a)

'''
 集合a = set(['a','b','c'])做下面的操作：

1 添加字符串'jay'到集合a里。

2 集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集。
'''
a = set(['a', 'b', 'c'])
a.add('jay')
print(a)

b = set(['b', 'e', 'f', 'g'])
# 第一种：
print(a | b)
# 第二种：
for i in b:
    a.add(i)
print(a)

'''
已知字典：ainfo = {'ab':'liming','ac':20}

完成下面的操作

1 使用2个方法，输出的结果：

ainfo = {'ab':'liming','ac':20,'sex':'man','age':20}

2 输出结果：['ab','ac']

3 输出结果：['liming',20]

4 通过2个方法返回键名ab对应的值。

5 通过2个方法删除键名ac对应的值。
'''
ainfo = {'ab': 'liming', 'ac': 20}
# 第一种：
ainfo['sex'] = 'man'
ainfo['age'] = 20
# 第二种：
ainfo.update({'sex': 'man'})
ainfo.update({'age': 20})
print(ainfo)

ainfo = {'ab': 'liming', 'ac': 20}
print(ainfo.keys())

print(ainfo.values())

print(ainfo.get('ab'))
print(list(ainfo.values())[0])

ainfo.pop('ac')
del ainfo['ac']
print(ainfo)
