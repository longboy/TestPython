from collections import namedtuple
User=namedtuple('User',['name','age','height','edu'])
user_tuple=('yy',34,157)
user=User(*user_tuple,"master")
print(user.name,user.age,user.height,user.edu)
