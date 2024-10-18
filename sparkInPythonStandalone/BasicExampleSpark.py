from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "Word Count Example")

# Read a text file into an RDD
rdd = sc.textFile("English-Quran-plain-text.txt")

# Split each line into words, then map each word to (word, 1)
word_counts = rdd.flatMap(lambda line: line.split(" ")) \
                 .map(lambda word: (word, 1)) \
                 .reduceByKey(lambda a, b: a + b).collect()

# Collect and print the word counts
#print(word_counts)
with open('word_count_output.txt','w') as output_file:
    for word,count in word_counts:
        output_file.write(f'{word}: {count}\n')
