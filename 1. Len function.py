# Len functions
# https://stackoverflow.com/questions/61761111/for-loop-for-defining-index-and-len-in-python

#+---------------------------------------------------------------------------------------- Len

# Len functie telt het aantal characters in een string
print (len('Chandrika'))

#output is 9. De functie telt alle karakters in de string. 

#+---------------------------------------------------------------------------------------- Len in List

# Len functions in list. 

listA = [3, 'go', 7.1]
listB = [4, 'hi', 1]
listC = listA + listB
print(len(listC))

# output is 6. De len functie telt hoeveel onderdelen er in de lijst zijn. 

#+----------------------------------------------------------------------------------------- Len and For Loop

# Len toepassing in een lijst als hier boven aangegeven. 

myList = [3, 12, "pizza", 3, 4]
print("myList heeft lengte", len(myList))

# Len() en index() in For Loop. 
for i in range(0, len(myList)):               # range() is een functie in de For Loop. 
  print("element met index", i, ":", myList[i])

