# BigData
To run hadoop Map reduce application
hadoop jar /home/master/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input file:///home/master/example.txt -output /data/example -mapper "python3 mapper.py" -reducer "python3 reducer.py"

This is an example to test hadoop map reduce
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-x.y.z.jar wordcount input.txt output

