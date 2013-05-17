#-*-coding: utf-8 -*-

import xlrd
import codecs
from generateBarcode import createBarCodes
import sys
from reportlab.pdfgen import canvas

def getDataFromExcel(filename):
    """
    f = codecs.open('startOutput.txt', 'w', 'utf-8')
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

    f.close()
    """
    
    c = canvas.Canvas("barcodes.pdf")

    old_stdout = sys.stdout 
    sys.stdout = open(filename, 'w')

    workbook = xlrd.open_workbook('xlrdTest.xls')#, encoding_override = "UTF-8")
    worksheet = workbook.sheet_by_name('Sheet2')
    num_rows = worksheet.nrows
    num_cells = worksheet.ncols

    column_ID, column_first_name, column_last_name = 1, 3, 4

    check = True
    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    curr_row = 0
    # get ID, first_name, last_name from excel to the lists
    while curr_row < num_rows :
        if worksheet.cell_type(curr_row, 0) != 0 :
            faculty = worksheet.cell_value(curr_row, 1)
            ID, first_name, last_name = [], [], []

            curr_row += 2
            while curr_row < num_rows and worksheet.cell_type(curr_row, 0) != 0 :
                tmp = str(worksheet.cell_value(curr_row, column_ID))
                tmp = tmp[0:10]
                ID.append(tmp)
                first_name.append(worksheet.cell_value(curr_row, column_first_name))
                last_name.append(worksheet.cell_value(curr_row, column_last_name))

                curr_row += 1

            print faculty.encode('utf-8')
            for x in range(0, len(ID)) :
                # print type(ID[x]), type(first_name[x]), type(last_name[x])
                print ID[x], first_name[x].encode('utf-8'), last_name[x].encode('utf-8')

            print ""

            if check :
                createBarCodes("1234567890", ID, first_name, last_name, faculty)
                check = False
        else :
            curr_row += 1

    # createBarCodes(barcode_value, ID, first_name, last_name, faculty):
    # createBarCodes("1234567890", ID, first_name, last_name, faculty)

    sys.stdout = old_stdout

if __name__ == "__main__":
    getDataFromExcel('startOutput.txt')
    
