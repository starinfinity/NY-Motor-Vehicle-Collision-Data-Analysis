NYPD-Data-analysis
Data Analysis using Map Reduce(Hadoop)

Files:
map.py		- mapper function for processing in hadoop
reduce.py	- reducer funtion for processing in hadoop
textfilewithallresult- result file containing final result
hadoop-streaming- hadoop jar file to stream python

Instructions:
I used spark to clean my data 

Step 2 :run the mapper and reducer files in hadoop


#this will process the data using hadoop
hadoop jar hadoop-streaming-3.1.0.3.0.0.0-1634.jar -file map.py -mapper map.py -file reduce.py -reducer reduce.py
 -input /path/to/the/cleaned/file/cleaninputfile.csv -output resultoutput.txt
 
 
 
 
 to view output
COMMAND: hadoop fs -cat /path/to/output/file/resultoutput.txt/*
