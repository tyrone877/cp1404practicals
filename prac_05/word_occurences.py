column_width = 0

text = input("Enter in text: ")

words = text.strip().split()

count_words = {}

for word in words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

for word in words:
    if len(word) > column_width:
        column_width = len(word)

for word, occurrences in count_words.items():
    print("{:{}} : {}".format(word, column_width, count_words[word]))
