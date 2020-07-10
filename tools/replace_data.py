# coding :utf8
'''
@Time    : 2020/7/8 18:46
@Author  : MaKaiQiang
@File    : replace_data.py
'''
from tools.write_excel import WriteExcel
from tools.get_excel_case import GetExcelCase
from tools.log import Logger
import re


class ReplaceData():
    def __init__(self, old_excel_data, write_file_name=r'E:\Auto-interface\data\case.xlsx', write_sheet_name='楼栋房屋'):
        self.write_excel = WriteExcel(file_name=write_file_name, sheet_name=write_sheet_name)
        self.log = Logger()
        self.old_excel_data = old_excel_data

    def replace_data(self, row, uuid=None, col=6):
        # self.log.logger.debug(f'长度{len(text)},text:{text}')
        if col == 6:
            compile_ = re.compile('[0-9a-z]{32}')
            old_body = self.old_excel_data[row]['json']
            compile_text = compile_.search(old_body).group(0)
        else:
            compile_ = re.compile('([0-9a-z]{32})/house')
            old_body = self.old_excel_data[row]['url']
            self.log.logger.debug(f'old_body:{old_body}')
            compile_text = compile_.search(old_body).group(1)
        # else:
        #     compile_ = re.compile('([0-9a-z]{32})')
        #     old_body = text[row]['url']
        #     old_params = text[row]['paramas']
        #     uuid = GetExcelCase(fileName=r'E:\Auto-interface\data\test_data.xlsx',sheetName='楼栋房屋').get_dict_data[0]
        #     self.log.logger.debug(f'get_uuid:{uuid}')
        #     self.log.logger.debug(f'old_paramas:{old_params}')
        #     compile_text = compile_.search(old_params).group(0)
        #     self.log.logger.debug(f'compile_text:{compile_text}')
        #     new_body = old_body.replace(compile_text, eval(str(uuid))[0])
        #     self.log.logger.debug(f'cnew_body:{new_body}')
        #     self.write_excel.write(row + 2, 4, new_body)
        #     col = 3

        self.log.logger.debug(f'get_excel:{compile_text}')
        new_body = old_body.replace(compile_text, eval(str(uuid))[0])
        self.log.logger.debug(eval(str(uuid))[0])
        self.write_excel.write(row + 2, col, new_body)


if __name__ == '__main__':
    r = ReplaceData()
