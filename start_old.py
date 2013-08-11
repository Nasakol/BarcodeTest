#-*-coding: utf-8 -*-

import xlrd
import codecs
from generateBarcode import createBarCodes
import sys
from reportlab.pdfgen import canvas

def getDataFromExcel():
    """ open excel and save data in seat No., ID, gender, first_name, last_name (type List)
    """

    c = canvas.Canvas("barcodes.pdf")

    old_stdout = sys.stdout 
    sys.stdout = open('startOutput.txt', 'w')

    workbook = xlrd.open_workbook('DataStudent.xls') #, encoding_override = "UTF-8")
    worksheet = workbook.sheet_by_name('Sheet2')
    num_rows = worksheet.nrows
    num_cells = worksheet.ncols

    column_seatNo, column_ID, column_gender, column_first_name, column_last_name = 0, 1, 2, 3, 4

    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    curr_row = 0
    # get seat No., ID, gender, first_name, last_name from excel to the lists
    while curr_row < num_rows :
        if worksheet.cell_type(curr_row, 0) != 0 :
            faculty = worksheet.cell_value(curr_row, 1)
            seatNo, ID, gender, first_name, last_name = [], [], [], [], []

            curr_row += 2
            while curr_row < num_rows and worksheet.cell_type(curr_row, 0) != 0 :
                tmp = str(worksheet.cell_value(curr_row, column_ID))[0:10]
                ID.append(tmp)
                seatNo.append(worksheet.cell_value(curr_row, column_seatNo))
                gender.append(worksheet.cell_value(curr_row, column_gender))
                first_name.append(worksheet.cell_value(curr_row, column_first_name))
                last_name.append(worksheet.cell_value(curr_row, column_last_name))

                curr_row += 1

            # print faculty.encode('utf-8')
            for x in range(0, len(ID)) :
                pass
                # print ID[x], first_name[x].encode('utf-8'), last_name[x].encode('utf-8')

            # print ""

            createBarCodes("1234567890", c, seatNo, ID, gender, first_name, last_name, faculty)
        else :
            curr_row += 1

    c.save()
    sys.stdout = old_stdout

if __name__ == "__main__":
    getDataFromExcel()
    
