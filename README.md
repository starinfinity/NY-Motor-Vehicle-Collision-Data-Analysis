Map-reduce

Motor Vehicle Collision Data Analyses using Map Reduce(Hadoop) 

Data:
https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95

Files:
map.py		- mapper function for processing in hadoop
reduce.py	- reducer funtion for processing in hadoop
textfilewithallresult- result file containing final result
hadoop-streaming- hadoop jar file to stream python

Instructions:
I used spark to clean my data which shoed in following repository
https://github.com/starinfinity/Data-Analysis-Spark-
you can use that cleaned file.

Step 2 :run the mapper and reducer files in hadoop


#this will process the data using hadoop
hadoop jar hadoop-streaming-3.1.0.3.0.0.0-1634.jar -file map.py -mapper map.py -file reduce.py -reducer reduce.py
 -input /path/to/the/cleaned/file/cleaninputfile.csv -output resultoutput.txt
 
 
 
 
 to view output
COMMAND: hadoop fs -cat /path/to/output/file/resultoutput.txt/*
