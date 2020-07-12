import collections
import re
from tools.get_excel_case import GetExcelCase

# 两种方法来给 namedtuple 定义方法名
# User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', ' nper1 nper2')
user = User({'floor_uuid': '123', 'uuid': '123123'}, {'floor_uuid': '123', 'uuid': '123123'}, )
compile_ = re.compile('[0-9a-z]{32}')
if __name__ == '__main__':
    url = 'http://192.168.9.238:15000/basedata-v1/project/090c24d6fcd248af8b8e76c4ef8b2c74/infrastructure/f633b7dce002461e832928dd4401e977/house'
    a=compile_.findall(url)
    print(a[-1])