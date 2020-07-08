# coding :utf8
'''
@Time    : 2020/7/8 18:46
@Author  : MaKaiQiang
@File    : replace_data.py
'''
from tools.write_excel import WriteExcel
from tools.get_excel_case import GetExcelCase
from tools.log import Logger


class ReplaceData():
    def __init__(self):
        self.get_excel = GetExcelCase(fileName=r'E:\Auto-interface\data\case.xlsx', sheetName='楼栋房屋')
        self.write_excel = WriteExcel(file_name=r'E:\Auto-interface\data\case.xlsx', sheet_name='楼栋房屋')
        self.log = Logger()

    def replace_data(self,row, uuid):
        text = self.get_excel.get_dict_data
        body = text[row]['json']
        body = body.replace('insuid', eval(str(uuid))[0])
        self.write_excel.write(row+2,6,body)
        self.log.logger.debug(f'get_excel:{body}')


if __name__ == '__main__':
    r = ReplaceData()

