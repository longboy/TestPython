from collections import defaultdict
# user_dict = {}
# users = ['aa','aa1','aa','bb','bb2','bb2','aa']
# for user in users:
#     user_dict.setdefault(user,0)
#     user_dict[user] += 1
# print(user_dict)

# default用法一：
# default_dict=defaultdict(int)
# users = ['aa','aa1','aa','bb','bb2','bb2','aa']
# for user in users:
#     default_dict[user] += 1
# print(default_dict)

# default用法二：
def gen_defaultdict():
    return {
        "name":"",
        "nums":0
    }
default_dict=defaultdict(gen_defaultdict)
default_dict["group1"]
print(default_dict)