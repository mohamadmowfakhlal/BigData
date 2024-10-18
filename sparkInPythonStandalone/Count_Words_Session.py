from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Step 1: Initialize SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Step 2: Read the text file into a DataFrame
# Make sure to replace 'path_to_text_file.txt' with the actual path of your file
df = spark.read.text("rockyou.txt")

# Step 3: Split each line into words and explode into individual rows
words_df = df.select(explode(split(df.value, " ")).alias("word"))

# Step 4: Count the total number of words
word_count = words_df.count()

# Print the total word count
print(f"Total number of words: {word_count}")

# Stop the Spark session
spark.stop()
