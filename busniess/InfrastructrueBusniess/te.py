import collections

# 两种方法来给 namedtuple 定义方法名
# User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', ' nper1 nper2')
user = User({'floor_uuid': '123', 'uuid': '123123'}, {'floor_uuid': '123', 'uuid': '123123'}, )

print(user.nper1.get('floor_uuid'))
