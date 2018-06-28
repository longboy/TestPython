# 异常
try:
    num = int(input("请输入num："))
    a = 100 / num
    print("计算结果：{0}".format(a))
except ZeroDivisionError as e:
    print("输入错误")
    print(e)
    exit()
except NameError as e:
    print("名字错了")
    print(e)
    exit()
except Exception as e:
    print("不知道什么错误")
    print(e)
    exit()
else:
    print("NO EXCEPTION")
finally:
    print("计算结束！！！！！")

