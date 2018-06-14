# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(row * col, end=" ")
#     print("")


def printline(row):
    for col in range(1, row + 1):
        print(row * col, end=" ")
    print("")


for row in range(1, 10):
    printline(row)
