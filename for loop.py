a = "python selenium"
char = "e"
for index in range(len(a)):
    if a[index] == char:
        print(f"the charecter {char} is present at the index {index}")
        break
###print words with odd length

lang = ["Python", "java" , "ruby" , "Pearl" , "php"]
for lang in lang:
    if lang.startswith('P'):
        print(lang)

names = ["bob", "max", "jhon", "eve", "steve"]
ind_dict = dict(enumerate(names))
print(ind_dict)

sentence1 = "hello everyone good afternoon"
words = sentence1.split()
d = {}
for word in words:
    d[word] = word[0]
    print(d)

