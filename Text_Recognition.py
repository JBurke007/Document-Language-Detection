from langdetect import detect
from langdetect import detect_langs
import os
import codecs

print "--Flat File Program Started--"

directory = "OUTPUT\\TEXT\\"

FlatFilesOutput = open(directory+"Flat_File_Output.csv", "w")
FlatFileErrorLog = open(directory+"Flat_File_Error_Log.csv", "w")

FlatFilesOutput.write("Filename,File Type,Language1,Language2,Language3"+"\n")
FlatFileErrorLog.write("Filename,File Type,Error_Message,Error_Output"+"\n")

counter = 1
filetype = "TEXT"

def textFileProcessing(filepath, encoding):
    fileContent = codecs.open(filepath, "r", encoding).read()
    return detect_langs(fileContent)
    
    
directoryLocation = "INPUT\\TEXT\\";
for filename in os.listdir(directoryLocation):
    #.write(filename+",")
    print counter,": ", filename
    fileToPass = str(directoryLocation+filename)
    if filename[0] != "~":
        try:
            langOutput = textFileProcessing(fileToPass, "utf-8")
            numLanguage = str(langOutput).count(':'); stopIter1 =  str(langOutput).find(':'); stopIter2 =  str(langOutput).find(':', stopIter1+1); stopIter3 =  str(langOutput).find(':', stopIter2+1)
            if numLanguage == 1:
                #print filename, "-", str(langOutput)[1:stopIter1]
                FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+",,")
            elif numLanguage == 2:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2] 
                FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+",")
            elif numLanguage == 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
            elif numLanguage > 3:
                #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
        except Exception as e:

            try:
                
                langOutput = textFileProcessing(fileToPass, "utf-16")
                numLanguage = str(langOutput).count(':'); stopIter1 =  str(langOutput).find(':'); stopIter2 =  str(langOutput).find(':', stopIter1+1); stopIter3 =  str(langOutput).find(':', stopIter2+1)
                if numLanguage == 1:
                    #print filename, "-", str(langOutput)[1:stopIter1]
                    FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+",,")
                elif numLanguage == 2:
                    #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2] 
                    FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+",")
                elif numLanguage == 3:
                    #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                    FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
                elif numLanguage > 3:
                    #print filename, "-", str(langOutput)[1:stopIter1], str(langOutput)[stopIter2-2:stopIter2], str(langOutput)[stopIter3-2:stopIter3] 
                    FlatFilesOutput.write(filename+","+filetype+","+str(langOutput)[1:stopIter1]+","+str(langOutput)[stopIter2-2:stopIter2]+","+str(langOutput)[stopIter3-2:stopIter3])
            except Exception as e:
                FlatFileErrorLog.write(filename+","+filetype+","+"File Encoding Issue"+","+str(e))            
    else:
        continue
    FlatFilesOutput.write("\n")
    FlatFileErrorLog.write("\n")
    counter +=1
    
FlatFilesOutput.close()
FlatFileErrorLog.close()
print "--Flat File Program Complete--"