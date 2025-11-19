def vowels(name):
 return name[0] in "aeiouAEIOU"
names = ["eve", "steve", "bob", "anna", "john"]
result = list(map(vowels, names))
print(result)



names = ["eve", "steve", "bob", "anna", "john"]
result = list(map(lambda name: name[0] in "aeiouAEIOU", names))
print(result)

########lengthe of the words inside the list to uppercase.....
names = ["eve", "steve", "bob", "anna", "john", "ABCE"]
result = list(map(lambda names: names.lower() , names))
print(result)

def uppercase(names):
 return names.lower()
names = ["eve", "steve", "bob", "anna", "john"]
result = list(map(lambda names: names.upper() , names))
print(result)

