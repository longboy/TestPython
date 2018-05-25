'''
习题1：

列表a = [11,22,24,29,30,32]
1 把28插入到列表的末端
2 在元素29后面插入元素57
3 把元素11修改成6
4 删除元素32
5 对列表从小到大排序

'''
print('第一题：')
a = [11, 22, 24, 29, 30, 32]
a.append(28)
print(a)

a.insert(-3, 57)
print(a)

a[0] = 6
print(a)

a.pop()
print(a)

a.sort()
'''
习题2：

列表b = [1,2,3,4,5]
1 用2种方法输出下面的结果：
[1,2,3,4,5,6,7,8]
2 用列表的2种方法返回结果：[5,4]
3 判断2是否在列表里
'''

b = [1, 2, 3, 4, 5]
# 第一种：
b.extend([6, 7, 8])
print(b)
# 第二种：
b = [1, 2, 3, 4, 5]
c = b + [6, 7, 8]
print(c)

# 第一种：
b = [1, 2, 3, 4, 5]
c = b[-1:-3:-1]
print(c)
# 第二种：
b = [1, 2, 3, 4, 5]
c = []
c.append(b.pop())
c.append(b.pop())
print(c)

print(2 in b)

'''
习题3：

b = [23,45,22,44,25,66,78]
用列表解析完成下面习题：
1 生成所有奇数组成的列表
2 输出结果: ['the content 23','the content 45']
3 输出结果: [25, 47, 24, 46, 27, 68, 80]
'''
print('第三题：')
b = [23, 45, 22, 44, 25, 66, 78]
c = [x for x in b if x % 2 == 1]
print(c)

d = ['the content %s' % x for x in b[:2]]
print(d)

e = [x + 2 for x in b]
print(e)
'''
习题4：

用range方法和列表推导的方法生成列表：
[11,22,33]
'''
print('第四题：')
y = [x * 11 for x in range(1, 4)]
print(y)
'''
习题5：

已知元组:a = (1,4,5,6,7)
1 判断元素4是否在元组里
2 把元素5修改成8
'''
print('第五题：')
a = (1, 4, 5, 6, 7)
print(4 in a)
b = list(a)
b[2] = 8
a = tuple(b)
print(a)
'''
习题6：

已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：
1 添加字符串对象'abc'到集合setinfo
2 删除集合setinfo里面的成员m
3 求2个集合的交集和并集
'''
print('第六题：')
setinfo = set('acbdfem')
finfo = set('sabcdef')

setinfo.add('abc')
print(setinfo)

setinfo.remove('m')
print(setinfo)

print(setinfo | finfo)
print(setinfo & finfo)

'''
习题7：

用字典的方式完成下面一个小型的学生管理系统。

1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
比如定义2个同学：
姓名：李明，年龄25，考试分数：语文80，数学75，英语85
姓名：张强，年龄23，考试分数：语文75，数学82，英语78
2 给学生添加一门python课程成绩，李明60分，张强：80分
3 把张强的数学成绩由82分改成89分
4 删除李明的年龄数据
5 对张强同学的课程分数按照从低到高排序输出。
6 外部删除学生所在的城市属性，不存在返回字符串 beijing
'''
print('第七题：')
student = {
    'liming': {
        'name': '李明', 'age': 25, 'score': {
            'chinese': 80, 'math': 75, 'english': 85
        }
    }
}
student['zhangqiang'] = {
    'name': '张强', 'age': 23, 'score': {
        'chinese': 75, 'math': 82, 'english': 78
    }
}
print(student)

student['liming']['score']['python'] = 60
student['zhangqiang']['score']['python'] = 80
print(student)

student['zhangqiang']['score']['math'] = 89
print(student['zhangqiang'])

# 第一种：
# student['liming'].pop('age')
# 第二种：
del student['liming']['age']
print(student['liming'])

binfo = list(student['zhangqiang']['score'].values())
binfo.sort()
print(binfo)

student.pop('city','beijing')
