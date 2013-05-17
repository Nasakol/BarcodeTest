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
pdfmetrics.registerFont(ttfonts.TTFont('Tahoma', 'c:\\Windows\\Fonts\\Tahoma.TTF'))
 
#----------------------------------------------------------------------
def createBarCodes(barcode_value, c, ID, first_name, last_name, faculty):
    """
    Create barcode from Excel and embed in a PDF
    """
    # c = canvas.Canvas("barcodes.pdf", pagesize=A4)
    c.setFont("Tahoma", 9) 
    # barcode39 = code39.Extended39(barcode_value)
 
    # # draw the eanbc13 code
    barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
    bounds = barcode_eanbc13.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]


    # d = Drawing(1000, 1000)
    # d.add(barcode_eanbc13)
    # d.add(barcode_eanbc132)
    # renderPDF.draw(d, c, 0.5*inch, 0.5*inch)

    # faculty = u'วิศวกรรมศาสตร์'.encode('utf-8')
    pos_y = 0
    index_y = 0
    max_number_in_a_row = 5
    index = 0
    while index < len(ID) :
        c.setFont("Tahoma", 11) 
        c.translate(0.4*inch, 9.7*inch)
        c.drawString(3.3*inch, 1.3*inch, faculty)
        c.setFontSize(9)

        index_y = pos_y = 0
        while index_y < 7 and index < len(ID):
            pos_x = index_x = 0
            while index_x < max_number_in_a_row and index < len(ID):
                # index = index_y*5 + index_x

                # generate Barcode
                barcode_eanbc13 = eanbc.Ean13BarcodeWidget( ID[index] )
                d = Drawing()
                d.add(barcode_eanbc13)

                #draw
                renderPDF.draw(d, c, (pos_x)*inch, -(pos_y)*inch)
                c.drawString((pos_x+0.1)*inch, -(pos_y+0.15)*inch, first_name[index] + " " + last_name[index]) # len my name is 46 (space is 1 length)
                
                #update
                pos_x += 1.55
                index_x += 1
                index += 1
            #update
            pos_y += 1.5
            index_y += 1
            # index += 1
        c.showPage()

    # c.showPage()
    # c.save()
 
if __name__ == "__main__":
    c = canvas.Canvas("barcodes.pdf")
    createBarCodes("1234567890", c, [], [], [], "")
    c.save()
