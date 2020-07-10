import collections
import re
from tools.get_excel_case import GetExcelCase
# 两种方法来给 namedtuple 定义方法名
# User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', ' nper1 nper2')
user = User({'floor_uuid': '123', 'uuid': '123123'}, {'floor_uuid': '123', 'uuid': '123123'}, )
compile_ = re.compile('([0-9a-z]{32})/house')
if __name__ == '__main__':
    excel_data = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋新增').get_dict_data
    print(excel_data)
    add_rows = GetExcelCase(fileName=r'E:\Auto-interface\data\infrastructure\infrastructure_case.xlsx', sheetName='楼栋房屋新增').get_rows
    print(add_rows)
    a=[i for i in range(add_rows-1)]
    print(a)