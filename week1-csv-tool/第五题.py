def longest_word(sentence):
    words = sentence.split()
    max_len = words[0]
    for w in words:
        if len(w) > len(max_len):
            max_len = w
    return max_len




print(longest_word("i love ptyhon ffffff"))

