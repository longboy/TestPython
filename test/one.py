'''
今天作业：

1.阅读str对象的help文档，并解决如下的问题。

1.1.有如下字符串。
    python是动态语言      
要求如下[请分别写出脚本]：
(1.)去掉该字符串下前面所有的空格。
(2.)去掉该字符串下后面所有的空格。
(3.)去掉该字符串2边的空格。

1.2有如下字符串

"abc"

（1）请将其全部大写。
（2）请将其全部小写。

2 怎么查看变量的类型是什么？
'''
import types

p = "    python是动态语言    "
# 去掉前面空格
# print (p.lstrip())
# 去掉后面空格
# print(p.rstrip())
# 去掉全部空格
print(p.strip())
ee = "   ddd   eee   ggg   djlgkjga   "
# print(ee.replace(" ",""))
print(ee.split())
a = "abc"
print(a.upper())
print(a.lower())
print(type(a))