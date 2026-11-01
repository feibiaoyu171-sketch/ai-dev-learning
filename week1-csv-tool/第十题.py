def word_lengths(sentence):
    words = sentence.split()
    words_dict = {}
    for word in words:
        words_dict[word] = len(word)

    return words_dict

print(word_lengths("hi hello nihao"))