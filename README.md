# BigData

Which commands used to start the Apache Hadoop framework?

In terminal in Resource manager machine.

Hadoop-demon.sh start namenode.
The command initiates the NameNode process, which runs on the HDFS name node of the Hadoop cluster.
This process is responsible for managing the file system namespace.

yarn-daemon start resourcemanager.
start the ResourceManager daemon in a Hadoop YARN (Yet Another Resource Negotiator) cluster.

yarn-daemon.sh start nodeManager.
Start node manager in resource manager machine.

Good practice
Create a bash script that run both commands.

In terminal in worker machine use 
hadoop-daemon.sh start datanode.
It used to start the DataNode daemon in a Hadoop cluster.
 
Start node manager in worker machine.
 yarn-daemon.sh start nodeManager.

Note 
To stop all services in the node you use stop-all.sh.
If it does not work, use kill -9 process number from jps command.


How to use Hadoop Distributed file system to save file in specific folder

How to create a folder in HDFS?
Hadoop fs -mkdir -p /data

How to upload a file from your machine to this folder that is located in hdfs?
Hdfs dfs -put rockyou.txt /data

How to remove the folder from HDFS?
Hdfs dfs -rm -r /data

How to list all folders in HDFS?
Hadoop fs -ls /

How to fomrmat the namenode?
 hadoop namenode -format

How to read file in HDFS?
hdfs dfs -cat /input_dir/[InputFile].txt

How to read row data in file in HDFS?
hdfs dfs -cat /input_dir/output/part-00000


To run hadoop Map reduce application
hadoop jar /home/master/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input file:///home/master/example.txt -output /data/example -mapper "python3 mapper.py" -reducer "python3 reducer.py"

This is an example to test hadoop map reduce
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-x.y.z.jar wordcount input.txt output
