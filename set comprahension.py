l = [1, 2, 3, 4, 5]
result = set()
for num in l:
    result.add(num ** 2)
print(result)


names = ["bob", "steve", "john", "hannah", "eve"]
s = set()
for name in names:
    s.add(len(name))
print(s)

names = ["bob", "steve", "john", "hannah", "eve"]
s = {len(name) for name in names}
print(s)
###################################
names = ["bob", "steve", "john", "hannah", "eve"]
s = set()
for char in names:
    s.add(char[0])
print(s)

s = { char[0] for char in names}
print(s)

#################################

sentence = "hi everyone how are you"
a = set()
words = sentence.split()
for word in words:
    a.add(word[-1])
print(a)

a ={word[-1] for word in words}
print(a)

########################set of even numbers from 1 to 21

k = set()
for num in range(1 , 21):
    if num % 2 == 0:
        k.add(num)
print(k)

k = {num for num in range(1, 21) if num % 2 == 0 }
print(k)

######################################## vowels
sentence = "Hello Everyone how are u good evening"
words = sentence.split()
vowels = set()
for word in words:
    if word[0] in "aeiouAEIOU":
        vowels.add(word)
print(vowels)


vowels = {word for word in words if word[0] in "aeiouAEIOU"}
print(vowels)

############################### print odd length words
sentence = "Hello Everyone how are u good evening"
words = sentence.split()
odd_length = set()
for word in words:
    if len(word) % 2 != 0:
        odd_length.add((word))
print(odd_length)

odd_length = {word for word in words if len(word) % 2 != 0}
print(odd_length)

##########################pallindrome
words = ["level", "hello", "malayalam", "mom", "python", "dad"]
a = set()
for word in words:
    if word == word[::-1]:
        a.add(word)
print(a)

a = {word for word in words if word == word[::-1]}
print(a)

########################starting with pP
language = ["Python", "java", "Pearl", "ruby", "Php", "javascript"]
start = set()
for word in language:
    if word.startswith(("p" , "P")):
        start.add(word)
print(start)

start = {word for word in language if word.startswith(("p" , "P"))}
print(start)

####################numbers only with the numbers
a = ["abc", "123", "hello", "12345", "9876", "120", "hello",
"hii", "657", "543"]
new_list = set()
for num in a:
    if num.isdigit():
        new_list.add(num)
print(new_list)

new_list = {num for num in a if num.isdigit()}
print(new_list)


######################create a list of True or False
#if the word is pallindrome append True
#else add Fasle
words = ["level", "hello", "malayalam", "mom", "python",
"dad"]
l= set()
for word in words:
    if word == word[::-1]:
      l.add(True)
else:
    l.add(False)
print(l)



l = {True if word == word[::-1] else False for word in words}
print(l)

###############################create a set of age if it is greaterthan 18 "adult" or else print minor
#syntax: for loop with if and else condition


ages = [12, 17, 18, 25, 10]
s = set()
for age in ages:
    if age >= 18:
        s.add("Adult")
    else:
        s.add("Minor")
print(s)

s = {"Adult" if age >= 18 else "Minor" for age in ages}
print(s)

#create a set of words
#if even returns reverse else keep it as it is

words = ["level", "hell", "malayalam", "mom", "python", "dad"]
t = set()
for word in words:
    if len(word) % 2 == 0:
        t.add(word[::-1])
    else:
        t.add(word)
        print(t)

        t = {word[::-1] if len(word) % 2 == 0 else word for word in words}
    print(t)

#######create a set by replacing negative numbers with 0
nums = [10, -5, 20, -3, 15, -9]
s = set()
for num in nums:
    if num >0:
        s.add(num)
    else:
        s.add(0)
print(s)

s = {num if num>0 else 0 for num in nums}
print(s)

##########set comprehension
#create a set
#if the number is even add 10 it
#else subtract 10 from it

nums = [13, 82, 23, 46, 19, 93, 29, 28, 10]
s = set()
for num in nums:
    if num % 2 == 0:
        s.add(num+10)
    else:
        s.add(num-10)
print(s)

s ={(num+10) if num % 2 == 0 else (num-10) for num in nums}
print(s)

sentence = "hi how are you good evening"
words = sentence.split()
t = set()
for word in words:
    t.add(word)
print(t)

a = (12, 8 , 4, 6, 7, 8, 4, 6, 8 , 12, "hello")
print(a.index(8))
print(a.index(4))


