import collections
import re
# 两种方法来给 namedtuple 定义方法名
# User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', ' nper1 nper2')
user = User({'floor_uuid': '123', 'uuid': '123123'}, {'floor_uuid': '123', 'uuid': '123123'}, )
compile_ = re.compile('([0-9a-z]{32})/house')
if __name__ == '__main__':

    a='http://192.168.9.238:15000/basedata-v1/project/090c24d6fcd248af8b8e76c4ef8b2c74/infrastructure/8c725195488b465e92999366118e63c8/house'
    b=compile_.search(a).group(1)
    print(len('ac8a051ecdb64a57b5799f8827fb68e5'))