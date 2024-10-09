# BigData
To run hadoop Mp reduce application
hadoop jar /home/master/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input file:///home/master/example.txt -output /data/example -mapper "python3 mapper.py" -reducer "python3 reducer.py"
