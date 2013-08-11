#-*-coding: utf-8 -*-

import xlrd
import xlwt
import codecs
from generateBarcode import createBarCodes
from generateBarcode import createBarCodes_reserve
import sys
from reportlab.pdfgen import canvas


def deleteall(lst_string):
    cnt = 1
    while lst_string.count('') > 0:
        lst_string.remove('')
        cnt += 1

def strip_all_whitespace(s):
    delimeter_list = ['\t', '.', " "]
    for deli in delimeter_list:
        lst = s.split(deli)
        deleteall(lst)
        s = ' '.join(lst)

    # for x in lst :
    #     print x
    return s


def new_excel(seatNo, ID, gender, first_name, last_name, seatName, filename):
    """old excel format is bad, create new excel
    """
    wb = xlwt.Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet('Sheet1')

    row = 0
    sheet1.write(row, 0, u"ลำดับ".encode('utf-8'))
    sheet1.write(row, 1, u"รหัสนิสิต".encode('utf-8'))
    # sheet1.write(row, 2, u"คำนำหน้า".encode('utf-8'))
    sheet1.write(row, 2, u"ชื่อ - นามสกุล".encode('utf-8'))
    sheet1.write(row, 3, u"เลขที่นั่ง".encode('utf-8'))
    for row in range(0, len(ID)):
        sheet1.write(row+1, 0, seatNo[row])
        sheet1.write(row+1, 1, ID[row])
        sheet1.write(row+1, 2, gender[row] + first_name[row] + " " + last_name[row])
        sheet1.write(row+1, 3, seatName[row])

    wb.save(filename + '_new.xls')


def convert_seatNo_to_seatName(seatNo):
    """ return Array of seatName ex. [ข1, ข2, ข3, ...]
    """
    row_name = u"ขคงจฉชญฐณดตถทธนบปผฝพฟภมยรลวศษสห"
    num_column = [36, 36, 39, 39, 36, 38, 39, 41, 42, 39, 39, 40, 42, 43, 40, 42, 42, 44, 40, 42, 42, 42, 44, 40, 40, 42, 42, 42, 38, 38, 38]
    seatName = []
    cnt = 0
    for row in range(0, len(row_name)):
        for column_name in range(1, num_column[row]+1):
            seatName.append(row_name[row].encode('utf-8') + str(column_name))
            cnt += 1
            if cnt == len(seatNo):
                return seatName


def getDataFromExcel(filename_excel, sheetname, filename):
    """ open excel and save data in seat No., ID, gender, first_name, last_name (type List)
        then createBarCodes
    """

    c = canvas.Canvas(filename + '.pdf')

    old_stdout = sys.stdout
    # sys.stdout = open('startOutput.txt', 'w')

    workbook = xlrd.open_workbook(filename_excel)  # , encoding_override = "UTF-8")
    worksheet = workbook.sheet_by_name(sheetname)
    num_rows = worksheet.nrows
    num_cells = worksheet.ncols

    column_seatNo, column_ID, column_gender, column_first_name, column_last_name = 0, 1, 2, 3, 4

    faculty = u"วิศวกรรมศาสตร์".encode('utf-8')


    # fix_list = [151, 161, 171, 181, 191, 201, 211, 221, 231, 238]


    # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
    curr_row = 0
    # get seat No., ID, gender, first_name, last_name from excel to the lists
    seatNo, ID, gender, first_name, last_name = [], [], [], [], []
    while curr_row < num_rows:
        if worksheet.cell_type(curr_row, 2) != 0 and worksheet.cell_type(curr_row, 0) != 0:
            # faculty = worksheet.cell_value(curr_row, 1)

            while curr_row < num_rows and worksheet.cell_type(curr_row, 2) != 0 and worksheet.cell_type(curr_row, 0) != 0:
                # seatNo, gender, first_name
                tmp_str = worksheet.cell_value(curr_row, 0).encode('utf-8')
                tmp_str = strip_all_whitespace(tmp_str)
                lst_sgf = tmp_str.split(' ', 2)

                # -----------=fix_list----------------
                # only print number in fix_list
                # if int(lst_sgf[0]) not in fix_list:
                #     curr_row += 1
                #     continue

                if len(lst_sgf) == 3:
                    seatNo.append(lst_sgf[0])
                    gender.append(lst_sgf[1])
                    first_name.append(lst_sgf[2])
                else:
                    print tmp_str + " error, T T"
                    print len(lst_sgf)
                    print lst_sgf

                last_name.append(worksheet.cell_value(curr_row, 1).encode('utf-8'))

                tmp_ID = worksheet.cell_value(curr_row, 2).encode('utf-8')
                ID.append(tmp_ID.replace(' ', ''))

                curr_row += 1

        else:
            curr_row += 1

    # createBarCodes("1234567890", c, seatNo, ID, gender, first_name, last_name, faculty)
    createBarCodes_reserve("1234567890", c, seatNo, ID, gender, first_name, last_name, faculty)

    # seatName = convert_seatNo_to_seatName(seatNo)
    # new_excel(seatNo, ID, gender, first_name, last_name, seatName, filename)

    c.save()
    sys.stdout = old_stdout

if __name__ == "__main__":
    # getDataFromExcel("55-21g.xls", "sheet2", "55-21g")
    # getDataFromExcel("55-21b.xls", "sheet2", "55-21b")
    # getDataFromExcel("55-21g.xls", "sheet2", "55-21g_reserve")
    getDataFromExcel("55-21b.xls", "sheet2", "55-21b_reserve")
