# BigData
To run hadoop Mp reduce application
hadoop jar /home/master/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input file:///home/master/example.txt -output /data/example -mapper "python3 mapper.py" -reducer "python3 reducer.py"


hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-x.y.z.jar wordcount input.txt output

[2024-10-14 03:20:52.190]Container exited with a non-zero exit code 1. Error file: prelaunch.err.
Last 4096 bytes of prelaunch.err :
Last 4096 bytes of stderr :
Error: Could not find or load main class org.apache.hadoop.mapred.YarnChild
Caused by: java.lang.ClassNotFoundException: org.apache.hadoop.mapred.YarnChild


[2024-10-14 03:20:52.190]Container exited with a non-zero exit code 1. Error file: prelaunch.err.
Last 4096 bytes of prelaunch.err :
Last 4096 bytes of stderr :
Error: Could not find or load main class org.apache.hadoop.mapred.YarnChild
Caused by: java.lang.ClassNotFoundException: org.apache.hadoop.mapred.YarnChild


Error Exception from container-launch.\nContainer id: container_1728466507784_0001_02_000001\nExit code: 1\n\n[2024-10-09 11:36:34.056]Container exited with a non-zero exit code 1. Error file: prelaunch.err.\nLast 4096 bytes of prelaunch.err :\nLast 4096 bytes of stderr :\nError: Could not find or load main class org.apache.hadoop.mapreduce.v2.app.MRAppMaster\nCaused by: java.lang.ClassNotFoundException: org.apache.hadoop.mapreduce.v2.app.MRAppMaster\n\nPlease check whether your <HADOOP_HOME>/etc/hadoop/mapred-site.xml contains the below configuration:\n<property>\n  <name>yarn.app.mapreduce.am.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n<property>\n  <name>mapreduce.map.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n<property>\n  <name>mapreduce.reduce.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n\n[2024-10-09 11:36:34.056]Container exited with a non-zero exit code 1. Error file: prelaunch.err.\nLast 4096 bytes of prelaunch.err :\nLast 4096 bytes of stderr :\nError: Could not find or load main class org.apache.hadoop.mapreduce.v2.app.MRAppMaster\nCaused by: java.lang.ClassNotFoundException: org.apache.hadoop.mapreduce.v2.app.MRAppMaster\n\nPlease check whether your <HADOOP_HOME>/etc/hadoop/mapred-site.xml contains the below configuration:\n<property>\n  <name>yarn.app.mapreduce.am.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n<property>\n  <name>mapreduce.map.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n<property>\n  <name>mapreduce.reduce.env</name>\n  <value>HADOOP_MAPRED_HOME\=${full path of your hadoop distribution directory}</value>\n</property>\n\nFor more detailed output\, check the application tracking page: http://master:8088/cluster/app/application_1728466507784_0001 Then click on links to logs of each attempt.\n. Failing the application.,totalAllocatedContainers=2


/share/hadoop/common/*:/share/hadoop/common/lib/*:/share/hadoop/mapreduce/*:/share/hadoop/mapreduce/lib/*:/home/master/hadoop/share/hadoop/hdfs/*:/home/master/hadoop/share/hadoop/hdfs/lib/*


<property>
    <name>yarn.application.classpath</name>
    <value>
        $HADOOP_HOME/etc/hadoop:
        $HADOOP_HOME/share/hadoop/common/*:
        $HADOOP_HOME/share/hadoop/common/lib/*:
        $HADOOP_HOME/share/hadoop/hdfs/*:
        $HADOOP_HOME/share/hadoop/hdfs/lib/*:
        $HADOOP_HOME/share/hadoop/mapreduce/*:
        $HADOOP_HOME/share/hadoop/mapreduce/lib/*:
        $HADOOP_HOME/share/hadoop/yarn/*:
        $HADOOP_HOME/share/hadoop/yarn/lib/*
    </value>
</property>



/share/hadoop/common/*:/share/hadoop/common/lib/*:/share/hadoop/mapreduce/*:/share/hadoop/mapreduce/lib/*:/home/master/hadoop1/share/hadoop/hdfs/*:/home/master/hadoop1/share/hadoop/hdfs/lib/*
