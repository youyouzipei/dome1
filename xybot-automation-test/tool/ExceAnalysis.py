'''
表格读取文件，主要是读取case表格中的数据
pip install xlrd==1.2.0 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
'''
import xlrd
class ExceRead():
    book = None
    sheel = None
    shname = None


    def __init__(self):
        self.open_excel()
        pass

    def open_excel(self,file="../data/case.xlsx"):
        """
        打开表格
        :param file:表格位置
        :return:
        """
        self.book = xlrd.open_workbook(file)
        pass

    def obtain_sheet(self):
        """
        获取所有表的表明
        :return:
        """
        self.shname= self.book.sheet_names()
        return self.shname

    def sheet_openxlrd(self,shname):
        """
        根据表明打开表
        :param shname:
        :return:
        """
        self.sheel = self.book.sheet_by_name(shname)

    def row_number(self):
        """
        获取行数
        :return:
        """
        nrwonum = self.sheel.nrows
        return nrwonum
    def nrows_data(self,nrwonum):
        """
        获取行数据
        :return:
        """
        rowdata = self.sheel.row_values(nrwonum)
        return rowdata
    def start(self,sheetname):
        """
        启动函数
        :param sheetname: Excel表明
        :return:
        """

        lst = []  # 存放处理后的数据
        self.sheet_openxlrd(sheetname)
        nrwonum = self.row_number()
        for j in range(0,nrwonum):
            rowdata = self.nrows_data(j)
            # print(rowdata)
            lst.append(rowdata)
        return lst


if __name__ == '__main__':
    ex = ExceRead()
    # print(ex.obtain_sheet())

    print( ex.start("开始界面"))

