#-*-coding: utf-8 -*-

import xlrd
import codecs

f = codecs.open('xlrdOutput.txt', 'w', 'utf-8')
print f

workbook = xlrd.open_workbook('xlrdTest.xls')#, encoding_override = "UTF-8")
worksheet = workbook.sheet_by_name('Sheet2')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
f.write( u"จำนวน rows: " + str(num_rows) + ", num_cells: " + str(num_cells) + '\r\n' )

curr_row = -1
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    f.write('Row:'+ str(curr_row) + "\r\n")
    curr_cell = -1
    while curr_cell < num_cells:
        curr_cell += 1
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_value = worksheet.cell_value(curr_row, curr_cell)
        f.write( ' ' + str(cell_type) + ': ' )

        if not isinstance(cell_value, unicode) :
            cell_value = unicode(cell_value)
        f.write( cell_value)
        f.write( "\r\n" )

# f.write( "\r\n" )
# f.write( u'ฉันรักไพธอน')
f.close()


# book = xlrd.open_workbook("test.xls")
# print "The number of worksheets is", book.nsheets
# print "Worksheet name(s):", book.sheet_names()
# sh = book.sheet_by_index(0)
# print sh.name, sh.nrows, sh.ncols
# # print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
# for rx in range(sh.nrows):
#     print sh.row(rx)
# # Refer to docs for more details.
# # Feedback on API is welcomed.

