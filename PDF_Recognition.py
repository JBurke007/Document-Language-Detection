from langdetect import detect
from langdetect import detect_langs
import os

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from pip._vendor.distlib.locators import DirectoryLocator
 
print "--PDF Program Started--"

directory = "OUTPUT\\PDF\\"

PDFFilesOutput = open(directory+"PDF_Output.csv", "w")
PDFFileErrorLog = open(directory+"PDF_Error_Log.csv", "w")

PDFFilesOutput.write("Filename,File Type,Language1,Language2,Language3"+"\n")
PDFFileErrorLog.write("Filename,File Type,Error_Message,Error_Output"+"\n")
 
counter = 1
filetype = "PDF"
def convert_pdf_to_txt(path, encoding):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = encoding
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
 
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
 
    text = retstr.getvalue()
 
    fp.close()
    device.close()
    retstr.close()
    return detect_langs(text)

directoryLocation = "INPUT\\PDF\\";
for filename in os.listdir(directoryLocation):
    print counter,": ", filename
    fileToPass = str(directoryLocation+filename)
    try:
        langOutput = convert_pdf_to_txt(fileToPass, "ascii")
        numLanguage = str(langOutput).count(':'); stopIter1 =  str(langOutput).find(':'); stopIter2 =  str(langOutput).find(':', stopIter1+1); stopIter3 =  str(langOutput).find(':', stopIter2+1)
        if numLanguage == 1:
            #print filename, "-", str(langOutput)[1:stopIter1]
            PDFFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+",,")
        elif numLanguage == 2:
            #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2] 
            PDFFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+",")
        elif numLanguage == 3:
            #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
            PDFFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
        elif numLanguage > 3:
            #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
            PDFFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
    
    except Exception as e:
        #print filename, "did not work"
        PDFFileErrorLog.write(filename+","+filetype+","+"File Encoding Issue"+","+str(e))
    
    PDFFilesOutput.write("\n")
    PDFFileErrorLog.write("\n")
    counter +=1
    
PDFFilesOutput.close()
PDFFileErrorLog.close()

print "--PDF Program Complete--"