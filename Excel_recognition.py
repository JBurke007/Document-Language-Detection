from langdetect import detect
from langdetect import detect_langs
import os
import xlrd

print "--Excel Program Started--"

directory = "OUTPUT\\EXCEL\\"

ExcelFilesOutput = open(directory+"Excel_Output.csv", "w")
ExcelFileErrorLog = open(directory+"Excel_Error_Log.csv", "w")

ExcelFilesOutput.write("Filename,File Type,Language1,Language2,Language3"+"\n")
ExcelFileErrorLog.write("Filename,File Type,Error_Message,Error_Output"+"\n")

counter = 1
filetype = "EXCEL"

def excel_processing(filename):
    workbook = xlrd.open_workbook(filename)
    holder = []
    for sheet in workbook.sheet_names():
        current_sheet = workbook.sheet_by_name(sheet)
        numRows = current_sheet.nrows
        numCols = current_sheet.ncols
    #     print numRows, numCols
    
        for row in range(0,numRows):
             for column in range(0,numCols):
                holder.append(current_sheet.cell(row,column).value)
  
    langHolder = ''.join(holder)
    return detect_langs(langHolder)

directoryLocation = "INPUT\\EXCEL\\"
for filename in os.listdir(directoryLocation):
    print counter,": ",filename
    fileToPass = str(directoryLocation+filename)
    if filename[0] != "~":
        try:
            langOutput = excel_processing(fileToPass)
            numLanguage = str(langOutput).count(':'); stopIter1 =  str(langOutput).find(':'); stopIter2 =  str(langOutput).find(':', stopIter1+1); stopIter3 =  str(langOutput).find(':', stopIter2+1)
            #print filename, "-",
            if numLanguage == 1:
                #print filename, "-", str(langOutput)[1:stopIter1]
                ExcelFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+",,")
            elif numLanguage == 2:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2] 
                ExcelFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+",")
            elif numLanguage == 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                ExcelFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
            elif numLanguage > 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                ExcelFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
        except Exception as e:
            #print filename, "did not work"
            ExcelFileErrorLog.write(filename+","+filetype+","+"File Encoding Issue"+","+str(e))
    else:
        continue
    ExcelFilesOutput.write("\n")
    ExcelFileErrorLog.write("\n")
    counter +=1
    
ExcelFilesOutput.close()
ExcelFileErrorLog.close()

print "--Excel Program Complete--"