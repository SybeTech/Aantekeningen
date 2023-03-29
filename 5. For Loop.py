# For Loop

# https://www.w3schools.com/python/python_for_loops.asp
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# Often the program needs to repeat some block several times. That's where the loops come in handy.
# For loops are always inclusive in Python: they always run over all elements of the iterator (other than exceptions such as break , etc.).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

words = ["I", "love", "my", "wife", "Chandrika"]

for i in words:
   print (i)

# output: I 
#         love
#         my
#         wife
#         Chandrika

words = ["I", "love", "my", "wife", "Chandrika"]
print (len(words))

# Hier telt hij over de lijst heen. Het antwoord is dus 5. 
# Er zijn 5 woorden in de lijst aanwezig. 

# In een for loop zou het dan zo zijn:

for i in range (len(words)):
   print (i)

# output: 0
#         1
#         2
#         3
#         4

# En dat klopt want hij telt de 5 elementen in de list. 


#+------------------------------------------------------------------------------------------------------ break

# break terminates the execution of a for or while loop. 
# Statements in the loop after the break statement do not execute. 
# In nested loops, break exits only from the loop in which it occurs. 
# Control passes to the statement that follows the end of that loop.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#+------------------------------------------------------------------------------------------------------ continue

# The continue keyword can be used in any of the loop control structures. 
# It causes the loop to immediately jump to the next iteration of the loop. 
# In a for loop, the continue keyword causes control to immediately jump to the update statement.
# Dit noemen we iteration vandaar dat men vaak i gebruikt in de for loop. 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":                         # Loop begint vanaf "banana" te lopen. 
    continue
  print(x)

# output:   banana
#           cherry


#+------------------------------------------------------------------------------------------------------ Loop over list 

# How to Loop over a list. 

letters = ["a", "b", "c", "d", "e", "f"]

for i in enumerate(letters):        # enumerate() (opsomming) letters worden gekoppeld aan een opsomming. 
  print(i)                          # Er ontstaat op deze manier een index (0, 'a') waarbij 0 index nummer en a eerste van de lijst enz. 

# Bij print(i[0]) wordt alleen de rij van de index geprint. 
# Bij print(i[1]) wordt alleen de rij van de lijst geprint. 
# Bij print(print(i[0], i[1]) worden beiden uitgeprint. 

#+------------------------------------------------------------------------------------------------------ Shortes word in a string 

s = 'Sybe is druk bezig met Python. Best wel moeilijk soms.'

def find_short(s):
  list = s.split()                  # Hierdoor wordt geitereerd over een lijst en niet een string. 
  lenght = float("inf")             # Use float(inf) as an integer to represent it as infinity.
  for word in list:                 # Is het instellen van de for loop. 
    if len(word) < lenght:          # Het eerst gevonden woord zal altijd kleiner zijn dan float("inf"). Dit is namelijk oneindig.
      lenght = len(word)            # 1. lenght wordt hier vastgesteld als het eerste woord in de lijst. In dit geval Sybe, dat is 4 letters. 
  return lenght                     # 2. Dan kijkt hij naar het tweede woord. Die is 2 letters. Dus nu wordt dit wordt vergeleken met het volgende woord. 
                                    # 3. Omdat deze kleiner is. 
  
print (find_short(s))

# Goed opletten met het plaatsen van de return functie. Deze moet onder for komen. Onder if dan telt hij alleen de letters van het eerste woord. 

#+------------------------------------------------------------------------------------------------------ split()

# Met split() word de string opgedeeld in een list. Zodat elk woord een aparte groep wordt. 

txt = "welcome to the jungle"
x = txt.split()
print(x)

# output: ['welcome', 'to', 'the', 'jungle']

#+------------------------------------------------------------------------------------------------------ Shortes word in a list

list_of_strings = ["Python", "Java", "JavaScript", "PHP", "R", "Rust"]
shortest = list_of_strings[0]

for word in list_of_strings:
  if len(word) < len(shortest):
    shortest = word

print('The shortest word from listOfStrings is:', shortest)

# output:  The shortest word from main_list is: R

sample_list = ["India","America","Australia","Russia","South Africa","UK"]

min_len = 100
shortest_element = ""
for element in sample_list:
    if(len(element) < min_len):
        min_len = len(element)
        shortest_element = element
        
print(shortest_element)

# output: U

#+------------------------------------------------------------------------------------------------------ Shortes word in a list in def

names = ["Hans", "Anna", "Vladimir", "Michael", "Ed", "Susan", "Janice", "Jo"]


def get_all_shortest_string(names):                     # Function. 
    shortest_strings = []                               # Start with an empty list. This is the identity element for list addition
    shortest_length = float("inf")                      # Start with a huge number. This is the identity element for the minimum() function
    for string in names:                                # Go through all strings.
        if len(string) < shortest_length:               # Found a shorter one?
            shortest_length = len(string)               # remember the length
            shortest_strings = []                       # Clear all longer ones
            shortest_strings.append(string)             # Add the one we just found ---> Hierdoor komt de eerste kleine waarde wel 2x in de lijst. Dit kan je weg laten. 
        if len(string) == shortest_length:              # Found one of the same length? 
            shortest_strings.append(string)             # Add it!
    return shortest_strings


# assert ["Ed", "Jo"] == get_all_shortest_strings(names)

print (get_all_shortest_string(names))

# De stappen die er genomen worden om het korste woord(en) te vinden. 

# 1.  Schrijf een functie waarin de code wordt verpakt. 
# 2.  Maak een lege lijst. Dit is element voor de identiteit om een lijst toe te voegen. 
# 3.  Maak een variabele met een oneindig nummer. Dat is dus float("inf").
# 4.  Schrijf een loop die door alle stringen gaat. For x in .... :
# 5.  Schrijft met het if statement een vergelijking waarbij er elke keer een kleinere waarde wordt gevonden. 
# 6.  Ondersteunt de vergelijking met het zoeken en onthouden van de kleinste waarde. 
# 7.  Verwijder alle waardes die langer zijn. Dit met de lege lijst shortst_strings [].
# 8.  (De waarde met de korste lengte wordt toevegoed aan de lijst shortest strings shortest_strings.append(string).)--> Kan worden weg gelaten. 
# 9.  Er kunnen meer waarden zijn met dezelfde len. Daarom een vergelijking opstellen die dezelfde waarden vindl, if len(string) == shortest_length:.
# 10. De gevonden waarden worden toegevoegd aan de lijst shortest_strings, shortest_strings.append(string).

#+------------------------------------------------------------------------------------------------------ Shortes word in a list in def part II

movies = [
"The Towering Inferno",
"Jaws", 
"Midway", 
"Star Wars", 
"Close Encounters of the Third Kind 1",
"Close Encounters of the Third Kind 2",
"Close Encounters of the Third Kind 3",
"Superman ",
"Indiana Jones", 
"E.T.", 
"I.T.", 
"U.T.", 
"Y.T.", 
"O.T.", 
"Born on the Fourth of July",
"Always",
"Presumed Innocent",
"Memoirs of a Geisha"
]

def shortest_name_movies(movies):
   temp = []
   infinity_number = float("inf")
   for word in movies:
      if len(word) < infinity_number:
         infinity_number = len(word)
         temp = []
      if len(word) == infinity_number:
         temp.append(word)
   return temp

print (shortest_name_movies(movies))


#+------------------------------------------------------------------------------------------------------ Longest word in a list in def 

def longest_name_movies(movies):
   number = 0
   temp = []
   for word in movies:
      if len(word) > number:
         number = len(word)
         temp = []
         temp.append(word)
      if len(word) == number:
         temp.append(word)
   return temp

print (longest_name_movies(movies))

#+------------------------------------------------------------------------------------------------------ Nested loop

# Een nested loop is een loop binnen in een loop (outer loop, inner loop).
# De buitenste loop heet de outer loop.  
# De binnenste loop heet de inner loop. 

for x in range(1, 10):
  print(x, end='')          # met de end='' komen de getallen niet onder elkaar maar naast elkaar te staan. 

for i in range (3):         # Door een loop in een loop te zetten wordt de inner loop door de outer loop drie keer herhaald.        
  for x in range(1, 10):
    print(x, end='')
  print()                   # Hierdoor wordt de loop onder elkaar gezet. 

# A nested loop is a loop inside another loop. 
# Although all kinds of loops can be nested, the most common nested loop involves for loops. 
# These loops are particularly useful when displaying multidimensional data. When using these loops, 
# the first iteration of the first loop will initialize, followed by the second loop.


# Voorbeeld van een nested loop:

wordlist = ['big', 'cats', 'like', 'really']
vowels = "aeiou"
for j in vowels:                                # Iteration over de variabele vowels
    count = 0
    for i in range(len(wordlist)):              # Iteration over de variabele woordenlijst. 
        if j in wordlist[i]:                    # Vergelijking opstellen wanneer de iteratie van je voorkomt in de iteratie van de woordelijst. 
            count += 1
    print(j, 'occurs', count, 'times')          # De uitkomst wordt geprint. 

         
#+------------------------------------------------------------------------------------------------------ count = count + 1 

# What is the role of count += 1 in the program?
# count += 1,  So every iteration and if the condition is True the variable "count" is updated by adding 1 into it.

# Counting in a for loop manually in Python 
# This is a three-step process:
# 1. Initialize a count variable and set it to a number.
# 2. Use a for loop to iterate over a sequence.
# 3. On each iteration, reassign the count variable to its current value plus N.

my_list = ['a', 'b', 'c']

count = 0                   # We declared a count variable and initially set it to 0.

for item in my_list:
    count += 1              # = count = count + 1 (+= is het teken om iets toe te voegen.)
    print(count)

print(count)  # 👉️ 3 (Hij telt eerst de gehele loop en geeft daarna het eind antwoord.)


# How do you count characters in a loop in Python?
# 1. string = "The best of both worlds";
# 2. count = 0;
# 3. Counts each character except space.
# 4. for i in range(0, len(string)):
# 5. if(string[i] != ' '):
# 6. count = count + 1;
# 7. Displays the total number of characters present in the given string.
# 8. print("Total number of characters in a string: " + str(count));

string = "The best of the worlds"
count = 0                                 # We declared a count variable and initially set it to 0.

for i in range(0, len(string)):
   if (string[i] != ' '):                 # Vergelijking die het aantal karakters weergeeft in de zin, geeft . 
      count = count + 1                   # Tel systeem elke keer + 1. 

print("Total number of characters in a string: " + str(count))  

#+------------------------------------------------------------------------------------------------------ range()

# Can we use range in for loop?
# for loops repeat a block of code for all of the values in a list, array, string, or range() . 
# We can use a range() to simplify writing a for loop. 
# The stop value of the range() must be specified, 
# but we can also modify the start ing value and the step between integers in the range().
# range is eigenlijk repetition (herhaling). Hier word een handeling meerdere keren uitgevoerd. 

for x in range(6):
  print(x)

# Voorbeeld met else statement aan het einde van een loop. 

for x in range(6):
  print(x)                    # Door de Tab zit de print functie in de body van de for loop. 
else:
  print("Finally finished!")  # Wanneer de loop eindigt word de print functie uitgevoerd. 
                              # Deze actie wordt niet herhaald want hij zit niet in de body van de for loop. 

for i in range(3):
  print("Sybe!! !!")
print("In the Spectrum.")

# output    Sybe !! !!     i = 0
#           Sybe !! !!     i = 1
#           Sybe !! !!     i = 2
#           In the spectrum.

# Lijst omgekeerd uitprinten. 

for i in range(20,0,-1):
    print(i)

#+------------------------------------------------------------------------------------------------------ iterating over list with range()

# Iterating over Lists with range()

# If you have to access the indices of a list, it doesn't seem to be a good idea to use the for loop to iterate over the lists. 
# We can access all the elements, but the index of an element is not available. However, 
# there is a way to access both the index of an element and the element itself. 
# The solution lies in using range() in combination with the length function len():

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21]
for i in range(len(fibonacci)):
    print(i,fibonacci[i])
print()

# Voorbeeld met range en len. 
# You can also use the range() class to count in a for loop.
# 

a_list = ['bobby', 'hadz', 'com']

for index in range(len(a_list)):    # The range class creates an iterator object of the specified length.
    # 0 bobby
    # 1 hadz
    # 2 com
    print(index, a_list[index])

# This approach is very similar to using enumerate(), 
# however, the enumerate function is more convenient and direct.

#+------------------------------------------------------------------------------------------------------ For loop om vowels te tellen

listname = remove_toto_albums= [
"The Towering Inferno",
"Jaws", 
"Midway", 
"Star Wars", 
"Close Encounters of the Third Kind",
"Superman ",
"Indiana Jones", 
"E.T.", 
"Born on the Fourth of July",
"Always",
"Presumed Innocent",
"Memoirs of a Geisha",
"Fahrenheit",
"The Seventh One",
"Toto XX",
"Falling in Between",
"Toto XIV",
"Old Is New"
]


def vowelCounter(listName):
    vowels = 'aeiouAEIOU'
    new = ''.join(listName)
    count = 0
    for i in range(0, len(new)):
        if new[i] in vowels:
            count += 1
    return count

print (vowelCounter(listname))

#+------------------------------------------------------------------------------------------------------ str.lower() - str.upper()

string = ('AAAAAAAAAAAAAAAAAAAAAAAAAA')
b = string.lower()

print (b)
list =  ["AAAAAAA", "BBBBBBBBB"]

# The most Pythonic way to convert a string list my_list to all lowercase strings is to use the str.lower()
# method inside a list comprehension expression like so: [x.lower() for x in my_list]. 
# The result is a new string list, all lowercase.

list_lower = [x.lower() for x in list]

print (list_lower)


#+------------------------------------------------------------------------------------------------------ working for loop most vowels. 

countries = [
    {"name": "Afghanistan", "code": "AF"},
    {"name": "land Islands", "code": "AX"},
    {"name": "Albania", "code": "AL"},
    {"name": "Algeria", "code": "DZ"},
    {"name": "American Samoa", "code": "AS"},
    {"name": "AndorrA", "code": "AD"},
    {"name": "Angola", "code": "AO"},
    {"name": "Anguilla", "code": "AI"},
    {"name": "Antarctica", "code": "AQ"},
    {"name": "Antigua and Barbuda", "code": "AG"},
    {"name": "Argentina", "code": "AR"},
    {"name": "Armenia", "code": "AM"},
    {"name": "Aruba", "code": "AW"},
    {"name": "Australia", "code": "AU"},
    {"name": "Austria", "code": "AT"},
    {"name": "Azerbaijan", "code": "AZ"},
    {"name": "Bahamas", "code": "BS"},
    {"name": "Bahrain", "code": "BH"},
    {"name": "Bangladesh", "code": "BD"},
    {"name": "Barbados", "code": "BB"},
    {"name": "Belarus", "code": "BY"},
    {"name": "Belgium", "code": "BE"},
    {"name": "Belize", "code": "BZ"}
]

result = []
vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
for country in countries:
    c = country['name']
    cnt = 0
    for x in c:
        if x in vowels:
            cnt += 1
    result.append((c, cnt))
result = sorted(result, key=lambda x: x[1],reverse=True)[:3]
print(result)


#+------------------------------------------------------------------------------------------------------ most vowels for loop (eigen)