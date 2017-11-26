from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

#converts pdf, returns its text content as a string
def convert(fname):
    pages=None
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    #print(text)
    return text 


#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.decode("utf-8").split(".")[-1]
        #print(type(fileExtension))
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            #print(type(txtDir))
            #print(type(pdf))
            textFilename = txtDir.decode("utf-8") + pdf.decode("utf-8") + ".txt"
            textFile = open(textFilename, "w", encoding="utf-8") #make text file
            textFile.write(text) #write text to text file

			
pdfDir = "C:/Users/tourist800/python/tf_idf/Dataset/"
txtDir = "C:/Users/tourist800/python/tf_idf/text_dataset/"
convertMultiple(pdfDir.encode("utf-8"),txtDir.encode("utf-8") )
