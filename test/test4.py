# 变量作用域和列表
a1 = 100


def fun(*args):
    print(a1)
    a2 = 99
    print(a2)


print(a1)
print("-------")
fun()

# globals，locals函数
# 全局变量，局部变量

a=100
b=99

