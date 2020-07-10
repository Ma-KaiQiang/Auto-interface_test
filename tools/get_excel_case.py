# coding:utf8
from tools.log import Logger
import xlrd


# import xlwt


class GetExcelCase(object):
    def __init__(self, fileName=r'E:\Auto-interface\data\case.xlsx', sheetName='云平台登录'):
        self.work_book = xlrd.open_workbook(fileName)
        self.table = self.work_book.sheet_by_name(sheetName)
        self.colNum = self.table.ncols
        self.keys = self.table.row_values(0)
        self.log = Logger(level='debug')

    @property
    def get_rows(self):
        rows = self.table.nrows
        if rows > 1:
            # self.log.logger.debug(f'row:{self.table.nrows}')
            return rows
        else:
            return None

    @property
    def get_dict_data(self):
        if self.get_rows <= 1:
            self.log.logger.debug('xlsx表的总行数小于1')
            return None
        else:
            r = []  # 定义列表变量，把读取的每行数据拼接到此列表中
            for row in range(1, self.get_rows):  # 对行进行循环读取数据，从第二行开始
                s = {}  # 定义字典变量
                values = self.table.row_values(row)  # 获取行的数据
                # self.log.logger.debug(f'values:{values}')
                for col in range(0, self.colNum):  # 对列进行循环读取数据
                    cell_value = values[col]
                    # self.log.logger.debug(f'cell_value:{cell_value}')
                    if isinstance(cell_value, (int, float)):  # 判断读取数据是否是整型或浮点型
                        cell_value = int(cell_value)  # 是，数据转换为整数
                    # self.log.logger.debug(self.keys)
                    s[self.keys[col]] = str(cell_value).strip()  # 获取到单元格数据(去掉头尾空格)和key组成键对值
                # 将每行数加入测试数据列表中,一遍写入数据调用
                s['row'] = row
                # self.log.logger.debug(f's{s}')
                # if s['execute'] == "1":
                r.append(s)  # 把获取到行的数据装入r列表中
            return r  # 返回整个表的数据


if __name__ == '__main__':
    g = GetExcelCase()
    d = g.get_dict_data
    print(d)
