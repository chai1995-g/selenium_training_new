t = (5, 1, 7, 8, 2, 4, 3)
print(sorted(t))
print(sorted(t, reverse=False))

s = {1, 6, 7, 2, 7, 9, 10, 23, 21, 14}
print(sorted(s))
print(sorted(s, reverse=False))

temperatures = [("banglore", 27),("Mysore",25), ("Manglore", 35), ("Delhi", 36),("Chennai", 34)]
print(sorted(temperatures))

temp = sorted(temperatures, key=lambda num: num[1])
print(temp)

### repeated words and count
words = ["a", "a", "hi", "world", "hello", "world", "hi", "world"]
d = {word : words.count(word) for word in words}
print(d)








