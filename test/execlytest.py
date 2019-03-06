import xlrd


class OperationExecl:
    def __init__(self, filename=None, sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = "../Logs/demo.xlsx"
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets内容
    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_table_rows(self):
        table = self.data
        return table.nrows

    # 获取某个单元格内容
    def get_cell_value(self, row, colx):
        return self.data.cell_value(row, colx)


if __name__ == '__main__':
    opers = OperationExecl()
    print(opers.get_table_rows())
    print(opers.get_cell_value(1, 2))
