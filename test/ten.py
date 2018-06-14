# Todo
'''
已知字典：
ainfo = {'b':'python','a':'haha','c':'hehe','f':'xiaoming'}
2.1 迭代字典，输出结果：
('a', 'haha')
('c', 'hehe')
('b', 'python')
('f', 'xiaoming')
2.2 用2种方法输出结果：
a
c
b
f
2.3 写出查找字典里面值等于'haha'的key的代码
'''
ainfo = {'b': 'python', 'a': 'haha', 'c': 'hehe', 'f': 'xiaoming'}

list=ainfo.items()
for key,value in list:
    print (key,',',value)
