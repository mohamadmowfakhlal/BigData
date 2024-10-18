from collections import Counter
import time
# Step 1: Read the file
input_file = "rockyou.txt"
output_file = "word_occurrences.txt"
start_time = time.time()
try:
    with open(input_file, "r", encoding="ISO-8859-1") as file:
        text = file.read()

    # Step 2: Clean and split the text into words
    words = text.split()  # Convert to lowercase and split into words

    # Step 3: Count the word occurrences
    word_count = Counter(words)
    counter = 0
    # Step 4: Save the result to another file
    with open(output_file, "w", encoding="ISO-8859-1") as file:
        file.write(f"Antal ord i alt: { len(words)}")
        for word, count in word_count.items():
            file.write(f"{counter}: {word}: {count}\n")
            counter = counter + 1

    print(f"Word occurrences successfully saved to {output_file}- {len(words)}")

except FileNotFoundError:
    print(f"File {input_file} not found.")
end_time = time.time()
# calculate and print the elapsed time
elapsed_time = end_time -start_time
print(f"Time taken to execute the program: {elapsed_time:.2f}")