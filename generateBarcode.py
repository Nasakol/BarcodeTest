# -*- coding: utf-8 -*-

from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, inch
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF

from reportlab.pdfbase import pdfmetrics, ttfonts

# only 'Tahoma' Font that can print Thai correctly
pdfmetrics.registerFont(ttfonts.TTFont('THSarabun', 'THSarabun.TTF'))
pdfmetrics.registerFont(ttfonts.TTFont('THSarabunBold', "THSarabun Bold.TTF"))

# import os
# if os.name == 'nt': 
#     pdfmetrics.registerFont(ttfonts.TTFont('Tahoma', 'c:\\Windows\\Fonts\\Tahoma.TTF'))
# else :
#     pdfmetrics.registerFont(ttfonts.TTFont('Tahoma', '/Library/Fonts/Tahoma.TTF'))
#----------------------------------------------------------------------

def createBarCodes(barcode_value, c, seatNo, ID, gender, first_name, last_name, faculty):
    """
    Create barcode from List and embed in a PDF
    """
    # c = canvas.Canvas("barcodes.pdf", pagesize=A4)
    c.setFont("THSarabun", 12) 

    max_column = 2
    max_row = 5
    card_width = 85*mm
    card_height = 52*mm

    index = 0
    while index < len(ID) :
        # set default 
        c.setFont("THSarabun", 12) 
        c.translate(10*mm, 287*mm)
        c.drawString(0, 3*mm, faculty)   # print Faculty at the top of page 
        index_last_of_page = min(len(seatNo)-1, index+9)
        c.drawString(150*mm, 3*mm, str(int(seatNo[index]))+" - "+ str(int(seatNo[index_last_of_page])))

        # draw border
        c.line(0,0,0,-card_height*5)
        c.line(card_width,0,card_width,-card_height*5)
        c.line(card_width*2,0,card_width*2,-card_height*5)
        index_y = pos_y = 0
        while(index_y < max_row+1) :
            c.line(0, pos_y, 2*card_width, pos_y)
            pos_y -= card_height
            index_y += 1

        index_x = pos_x = 0
        # one page
        while index_x < max_column :
            pos_y = index_y = 0
            while index_y < max_row and index < len(ID):
                # generate Barcode EAN13
                # barcode_eanbc13 = eanbc.Ean13BarcodeWidget( ID[index] )
                # d = Drawing()
                # d.add(barcode_eanbc13)
                c.setFont("THSarabunBold", 16) 
                c.drawString(pos_x+20*mm,pos_y-5*mm,u"พิธีพระราชทานปริญญาบัตร".encode('utf-8'))
                c.drawString(pos_x+22*mm,pos_y-11*mm,u"จุฬาลงกรณ์มหาวิทยาลัย".encode('utf-8'))
                c.setFont("THSarabun", 16) 

                #generage barcode 128
                barcode128 = code128.Code128(ID[index], barWidth = 0.5*mm, barHeight = 14*mm)
                barcode128.drawOn(c, pos_x+13*mm, (pos_y-28*mm)) 

                # draw
                # renderPDF.draw(d, c, (pos_x)*inch, -(pos_y)*inch)
                c.drawString(pos_x+10*mm, pos_y-35*mm, gender[index] + " " + first_name[index] + " " + last_name[index]) # len my name is 46 (space is 1 length)
                c.drawString(pos_x+10*mm, pos_y-35*mm - 6*mm, u"คณะ".encode('utf-8') + faculty.encode('utf-8'))
                c.drawString(pos_x+10*mm, pos_y-35*mm - 6*2*mm, ID[index])
                c.drawString(pos_x+55*mm, pos_y-35*mm - 6*2*mm, u"ลำดับที่ ".encode('utf-8')+str(int(seatNo[index])))
                
                #update
                pos_y -= card_height
                index_y += 1
                index += 1
            #update
            pos_x += card_width
            index_x += 1
        c.showPage()

    # c.showPage()
    # c.save()
 
if __name__ == "__main__":
    pass
    # c = canvas.Canvas("barcodes.pdf")
    # createBarCodes("1234567890", c, [], [], [], "")
    # c.save()
