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
    def __init__(self, old_excel_data, write_file_name, write_sheet_name):
        self.write_excel = WriteExcel(file_name=write_file_name, sheet_name=write_sheet_name)
        self.log = Logger()
        self.old_excel_data = old_excel_data

    def replace_data(self, row, uuid=None):
        self.log.logger.debug(f'replace_row:{row}')
        # 因为old_excel_data是一个列表是从0开始取数据所以-1
        replace_col = eval(self.old_excel_data[row - 1].get('replace'))
        self.log.logger.debug(f'replace_col:{replace_col}')
        key_list = [key[0] for key in replace_col.items()]
        if "json" in key_list:
            compile_ = re.compile('[0-9a-z]{32}')
            # 获取须替换行
            col = replace_col.get('json')
            for i in col:
                old_body = self.old_excel_data[i-2]['json']
                self.log.logger.debug(f'old_body:{old_body}')
                compile_text = compile_.search(old_body).group(0)
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.write_excel.write(i, 6, new_body)
        if "url" in key_list:
            compile_ = re.compile('([0-9a-z]{32})/house')
            col=replace_col.get('url')
            for i in col:
                old_body = self.old_excel_data[i - 2]['url']
                self.log.logger.debug(f'old_body:{old_body}')
                compile_text = compile_.search(old_body).group(1)
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.write_excel.write(i, 3, new_body)
        if "paramas" in key_list:
            compile_ = re.compile('[0-9a-z]{32}')
            # 获取须替换行
            col = replace_col.get('paramas')
            for i in col:
                old_body = self.old_excel_data[i - 2]['paramas']
                self.log.logger.debug(f'old_body:{old_body}')
                compile_text = compile_.search(old_body).group(0)
                new_body = old_body.replace(compile_text, eval(str(uuid))[0])
                self.write_excel.write(i, 4, new_body)

        # if replace_col[0] == 'json':
        #
        # if col1 == 6:
        #     compile_ = re.compile('[0-9a-z]{32}')
        #     old_body = self.old_excel_data[row]['json']
        #     compile_text = compile_.search(old_body).group(0)
        # else:
        #     compile_ = re.compile('([0-9a-z]{32})/house')
        #     old_body = self.old_excel_data[row]['url']
        #     self.log.logger.debug(f'old_body:{old_body}')
        #     compile_text = compile_.search(old_body).group(1)
        #
        # self.log.logger.debug(f'get_excel:{compile_text}')
        # new_body = old_body.replace(compile_text, eval(str(uuid))[0])
        # self.log.logger.debug(eval(str(uuid))[0])
        # self.write_excel.write(row + 2, col1, new_body)


if __name__ == '__main__':
    r = ReplaceData()
