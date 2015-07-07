from pyelasticsearch import ElasticSearch 
import time, codecs 

correct_counter = 0
failed_count = 0
data = []
failurelist = []

conn = ElasticSearch('http://127.0.0.1:9200') 
start = time.clock() 

input1 = raw_input ('Enter load data file name: ') 
input2 = raw_input ('Enter Project Name: ') 
input3 = raw_input ('Enter index name: ') 
input4 = raw_input ('How many columns does your data have? ') 
input5 = raw_input ('What is the delimiter? ') 
input6 = raw_input ('Enter file name for error output (.txt) ') 
input7 = raw_input ('Enter the codec that the data is formatted in: e.g. \'ascii'' ') 

FILENAME = codecs.open(input1, 'r', str(input7)) 
PROJECTNAME = str(input2) 
INDEXNAME = str(input3) 
NUM_OF_FIELDS = int(input4) 
DELIMITER = str(input5) 
ERRORFILEOUTPUT = open(input6, "w")

print "Running..."

for line in FILENAME:
	fields = line.split(DELIMITER) 
	if len(fields) == NUM_OF_FIELDS:
		data.append({
			"Filename" : fields[0].strip(),
			"File Type" : fields[1].strip(),
			"Language1" : fields[2].strip(),
			"Language2" : fields[3].strip(),
			"Language3" : fields[4].strip()
 			}) 
		try:
 			conn.bulk_index(PROJECTNAME,INDEXNAME,data)
			correct_counter += 1 
		except Exception as e: 
 			for i in data:
				failurelist.append(data)
 			failed_count += 1
 		data = []

if correct_counter!=0:
	print "\n",correct_counter," rows were successfully loaded into ES \n"
elif correct_counter==0:
	print "\n",correct_counter," rows were loaded into elasticsearch.\n" 

if (failed_count != 0) & (correct_counter != 0):
	print failed_count,"rows failed to load - check error output file to see the specific data"
elif (failed_count == 0) & (correct_counter != 0):
	print "No rows failed to load"
elif (failed_count != 0) & (correct_counter == 0):
	print "No rows were succesfully loaded to elasticsearch, check data"
elif (failed_count == 0) & (correct_counter == 0):
	print "Your load data was not processed, check to make sure the load data you attempted to load matches the map index that you sent to es"
else:
	print "Check data" 

for items in failurelist:
 	ERRORFILEOUTPUT.write(''+str(items)+"\n")

ERRORFILEOUTPUT.close()