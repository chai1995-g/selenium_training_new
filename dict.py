
sentence = "hi how r u hello how did u get here"
word1 = sentence.split()

word_count = {}
for word in word1:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

s = "its raining today and i love rain"
d = {}
for char in s:
    d[char] = s.count(char)
    print(d)

d = {char:s.count(char) for char in s}
print(d)


