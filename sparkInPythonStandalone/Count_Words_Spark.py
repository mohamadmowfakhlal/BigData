from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Word Count Example")

# Read a text file into an RDD
rdd = sc.textFile("rockyou.txt")

# Split each line into words, then map each word to (word, 1)
word_counts = rdd.flatMap(lambda line: line.split(" ")).count()

# Collect and print the word counts
print(word_counts)

