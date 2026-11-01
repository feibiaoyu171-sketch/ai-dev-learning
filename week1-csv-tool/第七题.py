def count_vowels(s):
    u = ["a","e","i","o","u"]
    count = 0
    for i in s:
        if i in u:
            count+=1
            print(i)
    return count

print(count_vowels("aeiou"))