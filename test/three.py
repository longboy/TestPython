'''
今天习题：

1 字符串:

a = 'abcd'

用2个方法取出字母d

2：

a = 'jay'

b = 'python'

用字符串拼接的方法输出：

my name is jay,i love python.

'''

a='abcd'
print(a[3])
print(a[-1])


a='jay'
b='python'
print(('%s'+ a +'%s'+ b)%('my name is ',',i love '))
