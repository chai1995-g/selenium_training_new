count = 0
while count <= 5:
    print("Hello")
    count += 1

start = 10
end = 1
while start >= end:
    print(start, end="")
    start -= 1

count = 0
while count <= 5:
    print(count)
    count += 1

    l = [1, 2, 3, 4, 5]
    index = 0
    while index < len(l):
        print(l[index])
        index += 1


for num in range(10,1):
    print("num")

for num in range(0, 22):
    if num % 3 == 0:
        print(num)

        for num in range(1, 21, 2):
            print(num)

string = "HeLlo WoRLd"

for char in string:
    if char.islower():
        print(char)

###########        #########

string = ""
for name in string:
    if name.islower():
        print(name)

s = " hello everyone"
for index in range(len(s)):
    if index % 2 == 0:
        print(s[index])
