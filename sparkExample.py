from pyspark import SparkConf, SparkContext

def main():
    # Initialize Spark
    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)

    # Read the input file
    input_file = "hdfs:///path/to/input.txt"  # Replace with your HDFS path
    text_file = sc.textFile(input_file)

    # Count words
    word_counts = (text_file.flatMap(lambda line: line.split(" "))
                            .map(lambda word: (word, 1))
                            .reduceByKey(lambda a, b: a + b))

    # Save the output
    output_file = "hdfs:///path/to/output"  # Replace with your desired output path
    word_counts.saveAsTextFile(output_file)

    # Stop Spark
    sc.stop()

if __name__ == "__main__":
    main()
