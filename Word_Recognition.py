from langdetect import detect
from langdetect import detect_langs
import os
import docx

print "--Word Program Started--"

directory = "OUTPUT\\WORD\\"

WordFilesOutput = open(directory+"Word_Output.csv", "w")
WordFileErrorLog = open(directory+"Word_Error_Log.csv", "w")

WordFilesOutput.write("Filename,File Type,Language1,Language2,Language3"+"\n")
WordFileErrorLog.write("Filename,File Type,Error_Message,Error_Output"+"\n")

counter = 1
filetype = "WORD"

def word_processing(filename):
    doc = docx.Document(filename)
    fullText = []
     
    for para in doc.paragraphs:
        fullText.append(para.text)
        
    langHolder = '\n'.join(fullText)
    return detect_langs(langHolder)
 
directoryLocation = "INPUT\\WORD\\"

for filename in os.listdir(directoryLocation):
    print counter,": ",filename
    fileToPass = str(directoryLocation+filename)
    if filename[0] != "~":
        try:
            #print filename, "-",  word_processing(fileToPass)
            langOutput = word_processing(fileToPass)
            numLanguage = str(langOutput).count(':'); stopIter1 =  str(langOutput).find(':'); stopIter2 =  str(langOutput).find(':', stopIter1+1); stopIter3 =  str(langOutput).find(':', stopIter2+1)
            #print filename, "-",
            if numLanguage == 1:
                #print filename, "-", str(langOutput)[1:stopIter1]
                WordFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+",,")
            elif numLanguage == 2:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2] 
                WordFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+",")
            elif numLanguage == 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                WordFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
            elif numLanguage > 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                WordFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
        except Exception as e:
            #print filename, "did not work"
            WordFileErrorLog.write(filename+","+filetype+","+"File Encoding Issue"+","+str(e))
    else:
        continue
    WordFilesOutput.write("\n")
    WordFileErrorLog.write("\n")
    counter +=1
    
WordFilesOutput.close()
WordFileErrorLog.close()

print "--Word Program Complete--"