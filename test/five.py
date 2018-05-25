'''
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。
'''
print('第一题：')
s = "i,am,lilei"
print(s[2:4])
print(s.split(',')[1])

'''
二.在python中，如何修改字符串？
'''
print('第二题：')
a = "my name is lili"
a = a.replace('lili', 'mary')
print(a)

'''
三.bool("2012" == 2012) 的结果是什么。
'''
print('第三题：')
b = bool('2012' == 2012)
print(b)

'''
四.已知一个文件 test.txt，内容如下：
____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________

1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
'''
print('第四题：')
v = "2012来了。\n2012不是世界末日。\n2012欢乐多。"
print(v)
print(len(v))
print(v.replace("\n", ""))
print(v.replace('2012', '2013'))
# 除法/需要用//代替，因为除法/会自动转型为浮点类型
print(v[len(v) // 2:len(v) // 2 + 5])
print(v[-2:])
print(v[:11])

'''
五.请用代码的形式描述python的引用机制。
'''
print('第五题：')
import sys

y = '1234'
print(id(y))
print(sys.getrefcount('1234'))

'''
六.已知如下代码
________

r = "中文编程"
t = r
k = r
r = "python编程"
t = u'%s' %r
q = "中文编程"
w = r
k = t
t2 = r.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数
'''
print("第六题：引用计数概念暂时不明白")
r = "中文编程"
t = r
k = r
r = "python编程"
t = u'%s' % r
q = "中文编程"
w = r
k = t
t2 = r.replace("中", "中")
print(sys.getrefcount("中文编程"))
print(sys.getrefcount('python编程'))

'''
七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
'''
print('第七题：')
a = "字符串拼接1"
b = "字符串拼接2"
c = a + b
print('第一种:' + c)
c = ''.join([a, b])
print('第二种:' + c)
c = "%s%s" % (a, b)
print('第三种:' + c)
c = "{a}{b}".format(a=a, b=b)
print('第四种:' + c + '\n')

n = "%s,%s" % (a, b)
print('逗号分隔:' + n + '\n')

print(len(n))
print(n[6])

'''
八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
'''
print('第八题：')
import string

print(string.digits)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.ascii_uppercase + string.ascii_lowercase + '\n')

strinfo = []
strinfo.append(string.digits)
strinfo.append(string.ascii_lowercase)
strinfo.append(string.punctuation)
strinfo.append(string.ascii_uppercase)
strinfo.append(string.ascii_lowercase)
# 第一种：
# print(''.join(strinfo))
# 第二种：
strinfo = "%s%s%s%s%s" % (
    string.digits, string.ascii_lowercase, string.punctuation, string.ascii_uppercase, string.ascii_lowercase)
print(strinfo)

'''
九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，
你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
'''
print('第九题：')
a1 = "i,am,a,boy,in,china"

a11c = "i,am,a,%(sex)s,in,%(country)s" % {'sex': 'girl', 'country': 'china'}
b11c = "i,am,a,{sex},in,{country}".format(sex='girl', country='india')
print(a11c)
print(b11c)

# 第一种：
print(a1[7:10])
print(a1[-5:])
# 第二种：
cInfo = a1.split(",")
print(cInfo[3])
print(cInfo[5])

print(a1.find('i'))

# 4.请找出"china"中的"i"字符在字符串a中的位置。(两种)
print(a1.find('i', a1.find('china')))
print(a1.rfind('i'))

print(a1.count(','))
