# In een lijst kun je verschillende datatypes plaatsen, zo kun je strings, integers en floats combineren. 
# Lijsten mogen ook leeg zijn. Tot slot kun je ook nog een lijst in een andere lijst plaatsen.

voorbeeld_lijst = ["Planten", 91, 25.2]     #[string, int, float]

# een lege lijst
boetes = []

# Functies die geschikt zijn voor lijsten. 

# Method	    Description
# append()	    Voegt een element toe aan het einde van een lijst.
# clear()	    Verwijdert alle elementen uit een lijst.
# copy()	    Creëert een kopie van een lijst.
# count()	    Telt hoevaak een bepaald element voorkomt in een lijst.
# extend()	    Voegt een lijst toe aan het einde van de huidige lijst.
# index()	    Achterhaalt de locatie van het eerste element dat aan de gedefinieerde omschrijving voldoet.
# insert()	    Voegt een element toe in een lijst op een specifieke positie.
# pop()	        Verwijdert een element op een specifieke locatie uit een lijst.
# remove()	    Verwijdert elementen die overeen komen met de gedefinieerde waarde.
# reverse()	    Keert de volgorde van een lijst om.
# sort()	    Sorteert een lijst.

#+----------------------------------------------------------------------------------------------------------------------------- append ()
# Voorbeeld append()
boodschappenlijst = ["Olijfolie", "Thee", "Wc papier", "Allesreiniger"]
recept = ["Meel", "Boter", "Zout"]
boodschappenlijst.append(recept)

print (boodschappenlijst)
#output ['Olijfolie', 'Thee', 'Wc papier', 'Allesreiniger', ['Meel', 'Boter', 'Zout']]

#+----------------------------------------------------------------------------------------------------------------------------- insert()

# Voorbeeld insert() functie. 
# Het extra lijstje wil je invoeren na "Olijfolie", "Thee" van de boodschappenlijst. 
# Dit kan met de insert functie. 

extra = ["Ketchup", "Drop"] 
boodschappenlijst.insert(2, extra)  # boodschappenlijst.insert(extra) werkt niet. Positie van insert moet worden aangegeven. 

print (boodschappenlijst)
# output ['Olijfolie', 'Thee', ['Ketchup', 'Drop'], 'Wc papier', 'Allesreiniger', ['Meel', 'Boter', 'Zout']]

#+----------------------------------------------------------------------------------------------------------------------------- extend()

# extend()

# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

prime_numbers = [2, 3, 5]
numbers = [1, 4]

# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)


print('List after extend():', numbers)

# Output: List after extend(): [1, 4, 2, 3, 5]
# Je voegt dus een waarde in de lijst toe. 
# Met append() komt er een lijst in een lijst. 
# Hetzelfde geld voor insert maar hiermee kan je de positie bepalen waar de lijst komt. 
# pop()
# Om items te verwijderen kun je de pop() en remove() methods gebruiken.

# Voorbeeld pop()
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

names = ['Sybe', 'Chandrika', 'Franzes', 'Gekke Henkie', 'Judith', 'Maria']

remove = names.pop(3)

print ('removed element:', remove)
print ('New list with cool people', names)

#+----------------------------------------------------------------------------------------------------------------------------- remove()

# remove()
# The remove() method removes the first matching element (which is passed as an argument) from the list.

prime_numbers = [2, 3, 5, 7, 9, 11]

prime_numbers.remove(9)
print('Updated List: ', prime_numbers)
# Output: Updated List:  [2, 3, 5, 7, 11]

# remove() Parameters
# The remove() method takes a single element as an argument and removes it from the list.
# If the element doesn't exist, it throws ValueError: list.remove(x): x not in list exception.

animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
animals.remove('dog')
animals.remove('dog')
animals.remove('dog')
print('Updated animals list: ', animals)

# output: Updated animals list:  ['cat', 'guinea pig']

#+----------------------------------------------------------------------------------------------------------------------------- index()

# index()
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')

print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')


print('The index of i:', index)

#+----------------------------------------------------------------------------------------------------------------------------- count()

#count()
# Telt hoe vaak een voorwerp voor komt in een lijst. 

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print (x)

#+----------------------------------------------------------------------------------------------------------------------------- reverse()

# reverse()
# The reverse() method reverses the elements of the list.

prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)

# Output: Reversed List: [7, 5, 3, 2]

#+----------------------------------------------------------------------------------------------------------------------------- sort()

# sort()
# Hiermee kan je lijsten sorteren. 

prime_numbers = [11, 3, 7, 5, 2]
 
# sorting the list in ascending order
prime_numbers.sort()

print(prime_numbers)

# Output: [2, 3, 5, 7, 11]

# syntax van sort = list.sort(key=..., reverse=...)

# sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison

# Python sorted()

# The sorted() function sorts the elements of a given iterable in a specific order 
# (ascending or descending) and returns it as a list.

numbers = [4, 2, 12, 8]

sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Output: [2, 4, 8, 12]

#+----------------------------------------------------------------------------------------------------------------------------- sort() with reverse= 

# syntax sort() vs. syntax sorted()
# sort() =      list.sort(key=..., reverse=...)
# sorted() =    sorted(list, key=..., reverse=...)

# Note: The simplest difference between sort() and sorted() is:
# sort() changes the list directly and doesn't return any value, while sorted() doesn't 
# change the list and returns the sorted list.

# sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison

# sort() Return Value
# The sort() method doesn't return any value. Rather, it changes the original list.
# If you want a function to return the sorted list rather than change the original list, use sorted().

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

# output Sorted list: ['a', 'e', 'i', 'o', 'u']

# list.sort(reverse=True) Hiermee wordt het tegenovergestelde uitgevoerd. 

vowels.sort(reverse=True)

print (vowels)

# Sort with custom function using key
# If you want your own implementation for sorting, the sort() method also accepts a key function as an optional parameter.
# Based on the results of the key function, you can sort the given list.

#+----------------------------------------------------------------------------------------------------------------------------- sort() with key= 

# list.sort(key=len)
# Alternatively for sorted:
# sorted(list, key=len)

# Here, len is Python's in-built function to count the length of an element.

# The list is sorted based on the length of each element, from lowest count to highest.

# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)         # In deze functie wordt het tweede element van de lijst gerangschikt. 

# print list
print('Sorted list:', random)

# output: Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

#+----------------------------------------------------------------------------------------------------------------------------- 


