# Tuples

# Using sorted()
# In Python, use the sorted() built-in function to sort a Tuple. 
# The tuple should be passed as an argument to the sorted() function. 
# The tuple items are sorted (by default) in ascending order in the list returned by the function. 
# We can use a tuple to convert this list data type to a tuple ().

# sorted(list, key=..., reverse=...)
# Note that key and reverse are two optional parameters:

# reverse: If this is set to “True”, the sorted list will be reversed or sorted in descending order.
# key: A function that acts as a kind of comparison key.

# The sorted() function sorts the elements of a given iterable in a specific order (ascending or descending) and returns it as a list.

# +=-------------------------------------------------------------------------------------------------------------------------------------- sorted()

numbers = [4, 2, 12, 8]

sorted_numbers = sorted(numbers)
print(sorted_numbers)
# Output: [2, 4, 8, 12]

words = ['Sybe', 'Chandrika', 'Maria', 'Franzes', 'Judith']

sorted_word = sorted(words)

print (sorted_word)
# output: ['Chandrika', 'Franzes', 'Judith', 'Maria', 'Sybe']

# Hierin is de syntax van sorted() --> sorted(iterable, key=None, reverse=False)
# sorted() can take a maximum of three parameters:
# 1. Iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
# 2. Reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
# 3. Key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

# +=-------------------------------------------------------------------------------------------------------------------------------------- reverse

# 2
words = ['Sybe', 'Chandrika', 'Maria', 'Franzes', 'Judith']
sorted_word = sorted(words, reverse = True)
print (sorted_word)

# 3
# take the second element for sort
def take_second(elem):                                      # Functie om het tweede element uit een lijst te halen (2, -->2), (1, -->4). 
    return elem[1]                                          # Hier telt hij het tweede element in de lijst namelijk: 0 -> 1. 
# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
sorted_list = sorted(random, key=take_second)               # Key functie = de functie die het tweede element uit de lijst pakt. 
# print list
print('Sorted list:', sorted_list)

# Output: Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]     # Is nu gesorteerd op de volgerde van nummer van het tweede element. 

# https://www.programiz.com/python-programming/methods/built-in/sorted

# +=-------------------------------------------------------------------------------------------------------------------------------------- lambda function

sample = [('f', 90), ('g', 84), ('d', 92), ('a', 96)]
sample.sort(key = lambda i:i[1], reverse = True)
print(sample)
 
# Output : [('a', 96), ('d', 92), ('f', 90), ('g', 84)]

def second_item(data):
    return data[1]

sample = [(1, 7, 3), (4, 9, 6), (7, 3, 9)]
sample.sort(key = second_item)
print(sample)
 
# Output : [(7, 3, 9), (1, 7, 3), (4, 9, 6)]

# https://learnpython.com/blog/sort-tuples-in-python/


