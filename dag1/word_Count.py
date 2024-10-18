from collections import Counter

counter = Counter()
with open('rockyou.txt','r', encoding="ISO-8859-1") as file:
    for line in file:
        words = line.split()
        counter.update(words)
counting = 0
with open('word_count_output.txt','w', encoding="ISO-8859-1") as output_file:
    for word,count in counter.items():
        output_file.write(f'{counting} {word}: {count}\n')
        counting = counting + 1

