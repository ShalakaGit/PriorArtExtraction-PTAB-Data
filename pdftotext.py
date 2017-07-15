from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + "\\" + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            name = pdf + ".txt"
            textFilename = os.path.join(txtDir,name)
            #textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w") #make text file
            textFile.write(text) #write text to text file
 
lDirs = ["D:\PTAB Data Mining\Data2017\PTAB_20170428_WK17\PTAB_20170422_20170428\PDF_image",
"D:\PTAB Data Mining\Data2017\PTAB_20170505_WK18\PTAB_20170429_20170505\PDF_image"] 
lTxtDirs = ["D:\\PTAB Data Mining\\Data2017\\PTAB_20170602_WK17_Output","D:\\PTAB Data Mining\\Data2017\\PTAB_20170602_WK18_Output"]

 
pdfDir = "D:\PTAB Data Mining\Convert\Convert2"
#"D:\PTAB Data Mining\Data2017\PTAB_20170512_WK19\PTAB_20170506_20170512\PDF_image"
#"D:\PTAB Data Mining\Data2017\PTAB_20170519_WK20\PTAB_20170513_20170519\PDF_image"
#"D:\PTAB Data Mining\Data2017\PTAB_20170526_WK21\PTAB_20170520_20170526\PDF_image"
txtDir = "D:\PTAB Data Mining\Convert\Convert2"

convertMultiple(pdfDir, txtDir)