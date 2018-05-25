from collections import namedtuple
User=namedtuple('User',["name","age","height"])
user=User(name="bv",age=13,height=134)
print(user.name,user.height,user.age)
