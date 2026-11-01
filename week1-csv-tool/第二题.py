def count_words(sentence):
    words = sentence.split()
    counts = {}
    for w in words:
        if w in counts:
            counts[w] = 1+counts[w]
        else:
            counts[w]=1
    return counts
sentence = "he he he she she me"
print(count_words(sentence))