"""
Excel报告生成
"""
import time

from xlutils import copy
import xlrd

class TestReportExcel():
    def __init__(self):
        book = xlrd.open_workbook("../data/case.xlsx")
        self.copy_book = copy.copy(book)
        pass

    def add_copy_excel(self,row,col,data,values=0):
        """
        新值写入excel表格
        :param row: 行
        :param col: 列
        :param data: 值
        :param values: 表下标
        :return:
        """
        # print(row,col,type(data),data)
        copy_sheet = self.copy_book.get_sheet(values)
        copy_sheet.write(row,col,data)

        pass
    def save_excel(self):
        timedata  = time.strftime("%Y-%m-%d %H-%M-%S")
        self.copy_book.save("../data/case_result%s.xls"%(timedata))

if __name__ == '__main__':
    tre = TestReportExcel()
    for i in range(1,4):
        tre.add_copy_excel(i,9,888)
    tre.save_excel()
