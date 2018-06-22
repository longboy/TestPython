'''
汉罗塔
n=塔数
a=第一个塔，开始的塔
b=第二塔，中间过渡塔
c=第三个塔，目标塔
'''


def hano(n, a, b, c):
    # 当塔数为1的时候
    if n == 1:
        print(a, "-->", c)
        return None
    # 当塔数为2的时候
    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        return None
    # a塔借助c塔放到b塔上
    hano(n - 1, a, c, b)
    # b塔借助a塔放到c塔上
    hano(n - 1, b, a, c)


a = "A"
b = "B"
c = "C"
n = 1
print("n=1时")
hano(n, a, b, c)
n = 2
print("n=2时")
hano(n, a, b, c)
n = 3
print("n=3时")
hano(n, a, b, c)
