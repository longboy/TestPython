'''
今天习题：
1 ：
info = 'abc'
info[2] = 'd'
结果是什么，为什么会报错呢?

2 如果要把上面的字符串info里面的c替换成d，要怎么操作呢？

3 下面2个变量 
a = '1'
b = 2
print a + b 的结果是什么，为什么会出现这个结果，如果希望结果是3，要怎么操作？
'''
# 方法一：
# info='abc'
# info=info.replace('c','d')
# print(info)
# 方法二：
info = 'abc'
l = list(info)
l[2] = 'd'
info = "".join(l)
print(info)

a = '1'
b = 2
print(int(a) + b)
