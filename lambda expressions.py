#####odd or even number
number = lambda x: "Even" if x % 2 == 0 else "Odd"
print(number(5))
print(number(7))

######pallindrome program
ispallindrome = lambda x: x == x[::-1]
print(ispallindrome("level"))
print(ispallindrome("hello"))

#######chedckign whether string is present in
is_present = lambda s, sub: sub in s
print(is_present("hi hello" , "hello"))
print(is_present("hi hello" , "how"))

##########converting a number to positive
convert_positive = lambda x: abs(x)
print(convert_positive(-1))

