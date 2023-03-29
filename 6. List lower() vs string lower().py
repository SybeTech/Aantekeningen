string = ('AAAAAAAAAAAAAAAAAAAAAAAAAA')
b = string.lower()

print (b)
list =  ["AAAAAAA", "BBBBBBBBB"]

# The most Pythonic way to convert a string list my_list to all lowercase strings is to use the str.lower()
# method inside a list comprehension expression like so: [x.lower() for x in my_list]. 
# The result is a new string list, all lowercase.

list_lower = [x.lower() for x in list]

print (list_lower)

