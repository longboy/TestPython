'''

习题一：

1 用while语句的2种方法输出数字：1到10
2 用for语句和continue 输出结果：1 3 5 7 9
'''
x = 1
while x <= 10:
    print(x)
    x += 1
print('-----------------------')
for i in range(10):
    if i % 2 == 1:
        print(i)
    else:
        continue

'''
习题二：假设有列表

a = [1,2,3,4,5,6]

1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，

输出字符串'not find'

2 用while语句操作上面的列表a，输出下面结果：

[2,3,4,5,6,7]
'''
print('----------------------')
a = [1, 2, 3, 4, 5, 6]
for b in a:
    if b == 8:
        print('find')
    else:
        print('not find')
print('-----------------------')

a = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(a):
    a[i] = a[i] + 1
    i += 1
print(a)

'''
1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
1.1 请将a字符串的大写改为小写，小写改为大写。
1.2 请将a字符串的数字取出，并输出成一个新的字符串。
1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
    并输出成一个字典。 例 {'a':4,'b':2}
1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符串。
    保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，
    请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
1.9 输出a字符串出现频率最高的字母
'''
print('-----------------------')
# 1
a = "aAsmr3idd4bgs7Dlsf9eAF"
# 大写转小写，小写转大写
print(a.swapcase())
# 2
aa = ''.join([i for i in a if i.isdigit()])
print(aa)
# 3
print({x: a.count(x) for x in set(a.lower())})
# 4
l = [i for i in set(a)]
l.sort(key=list(a).index)
print(''.join(l))
# 5
print(a[::-1])
# 6
a = "aAsmr3idd4bgs7Dlsf9eAF"
l = sorted(a)
upper_list = []
lower_list = []
for x in l:
    if x.isupper():
        upper_list.append(x)
    elif x.islower():
        lower_list.append(x)
    else:
        pass
print(upper_list)
print(lower_list)
for y in upper_list:
    y_lower = y.lower()
    if y_lower in lower_list:
        lower_list.insert(lower_list.index(y_lower), y)

print(''.join(lower_list))
# 7请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False
# 第一种：根据集合长度判断
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = 'boy'
l = list(b)
u = set(a)
u.update(l)
print(len(u) == len(l))
# 第二种：用issubset方法
print(set('boy').issubset(set(a)))
# 8
# 第一种：
a = "aAsmr3idd4bgs7Dlsf9eAF"
s = ['boy', 'girl', 'bird', 'dirty']
u = set(a)
for i in s:
    u.update(i)
print(len(set(a)) == len(u))
# 第二种：
a = "aAsmr3idd4bgs7Dlsf9eAF"
s = ['boy', 'girl', 'bird', 'dirty']
u = ''.join(s)
print(set(u).issubset(set(a)))
# 9 输出a字符串出现频率最高的字母
l = [(x, a.count(x)) for x in set(a)]

l.sort(key=lambda k: k[1], reverse=True)

print(l[0][0])
'''

2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。

3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
 
4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.

'''

# g=open('a.txt','w')
# g.write('dfdfgdgag\ndfsdsfsdf')
# g.close()

