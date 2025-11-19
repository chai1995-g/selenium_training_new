names = ["steve" , "eve" , "bob"]
char =[]
for name in names:
    char.append(len(name))
print(char)

names = ["steve" , "eve" , "bob"]
char =[len(name) for name in names]
print(char)

sentence = "hello everyone how are you doing good evening"
words = sentence.split()
for word in words:
    if word[0] in "aeiou":
        print(word)

sentence = "hello everyone how are you doing good evening"
words = sentence.split()
vowel = [word for word in words if word[0] in "aeiou"]
print(vowel)

words = ["level", "malayalam", "python"]
palin = [word for word in words if word == word[::-1]]
print(palin)

words = ["level", "malayalam", "python"]
for word in words:
    if word == word[::-1]:
        print(word)

        words = ["level", "hello", "malayalam", "mom", "python"]
        word1 = [word1[::-1] if len(word1) % 2 == 0 else word1 for word1 in words]
        print(word1)






a = ["abc", "123", "hello", "12345", "9876", "hii"]

for num in a:
    if num.isdigit():
     print(num)

a = ["abc", "123", "hello", "12345", "9876", "hii"]
l=[]
num = [num for num in a if num.isdigit()]
print(num)

sentence = "hi how r u hello how did u get here"
word_d = sentence.split()
count = {}

for word in word_d:
    if word in count:
        print(word)

        