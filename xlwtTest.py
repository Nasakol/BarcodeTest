from tempfile import TemporaryFile
from xlwt import Workbook
import xlrd
from xlutils.copy import copy

rb = xlrd.open_workbook('simple.xls')
rs = rb.sheet_by_index(0)
wb = copy(rb)
sheet1 = wb.get_sheet(0)
# sheet1 = book.add_sheet('Sheet 1')
# book.add_sheet('Sheet 2')
sheet1.write(10, 0, '')
sheet1.write(10, 1, 'B1')

# print sheet1.cell_type(10, 0)

# sheet2 = book.get_sheet(1)
# sheet2.row(0).write(0,'Sheet 2 A1')
# sheet2.row(0).write(1,'Sheet 2 B1')
# sheet2.flush_row_data()
# sheet2.write(1,0,'Sheet 2 A3')
# sheet2.col(0).width = 5000
# sheet2.col(0).hidden = True
wb.save('simple2.xls')
# book.save(TemporaryFile())
