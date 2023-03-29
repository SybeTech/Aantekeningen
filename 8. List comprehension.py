# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# List comprehension

# Lijsten staan tussen [] en e elementen worden gescheiden door , 
# Een list comphrehension staat tussen [] en wordt gestart met een statement gevolgd door een For Loop. 


# [expr for val in collection] De eerste expressie [expr] genereert de elementen in de lijst.
# [for val in collection] Dit wordt gevolgd door een For loop die over de data heen loopt. 
# Dit evalueert de expressie voor elk item in de collectie. 
# Waneer je specifieke data wil toevoegen voor een bepaalde waarde kan je een if-statment toevoegen. 
# Dit is dan het resultaat. [expr for val in collection if <test>]
# De expressie wordt aan de lijst toegevoegd alleen als het if statement correct is. 
# Er kunnen meerdere if clausules worden toegevoegd. [expr for val in collection if <test1> and <test2>] 
# Er kan over meerdere collecties heen geloopt worden. [expr for val 1 in collection1 and val2 in collection 2]


# +=----------------------------------------------------------------------------------------------------------------------------- voorbeeld list comprehension

# Voorbeeld #1 Maak een vierkant van de eerste 100 integers. 

# Maak er eerst een zonder list comphrensions. Dus schrijf de For Loop uit. 

squares = []                    # maak eerst een lege lijst genaamd squares. 
for i in range(1, 101):         # Loop over de eerste 100 positieve integers. 
        squares.append(i**2)    # Voeg i toe aan de nieuwe lijst die je gemaakt hebt. i wordt nu in het kwadraat gezet **2

print (squares)

# Schrijf deze code nu uit met list comprehensions. 

squares2 = [ i**2 for i in range(1,101)]    # Eerst wordt de expressie geschreven voor elk onderdeel (term of the list) van de lijst. 

print (squares2)

# +=----------------------------------------------------------------------------------------------------------------------------- voorbeeld list comprehension

names = ['Chandrika', 'Sybe', 'Judith', 'Maria', 'Franzes']

for i in names:
    print(i)

[print(i) for i in names]                       # Dit is list comprehension. Uitkomst is hetzelfde als bovenstaande stukje code.


# Opdracht om de list names in hoofdletters te schrijven. 

for i in names:
    i = i.upper()
print (names) 

# Deze code werkt niet op deze manier. Er gebeurd niets. 
# Om de code werkzaam te maken gaan we een lege lijst gebruiken. 

names = ['Chandrika', 'Sybe', 'Judith', 'Maria', 'Franzes']
new_names = []                                                              # Dit is de lege lijst. 

for i in names:                                                             # For loop die itereert over names. 
    i = i.upper()                                                           # Code om de variabele te veranderen in hoofdletters. 
    new_names.append(i)                                                     # Je voegt nu de nieuwe lijst toe met append() aan de lege lijst new_names
    names = new_names                                                       # Reasign names voor new_names. Deze vervangt names voor new_names. 
print (names) 

# Met list comprehension kan je de bovenstaande code samenvatten in 1 zin. 

names = [i.upper() for i in names]  # Door de code te beginnen met [] wordt er direct een nieuwe lijst gevormd. 
print (names)

# +=----------------------------------------------------------------------------------------------------------------------------- voorbeeld list comprehension

bits = [False, True, False, False, True, False, False, True ]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

super_bits = [ 1 if b == True else 0 for b in bits]

print(bits)
print(new_bits)
print(super_bits)

# +=----------------------------------------------------------------------------------------------------------------------------- string manupiltion

my_string = "HelloMyNameIsSybeFranzes"
my_string = [i for i in my_string]
print (my_string)
# output ['H', 'e', 'l', 'l', 'o', 'M', 'y', 'N', 'a', 'm', 'e', 'I', 's', 'S', 'y', 'b', 'e', 'F', 'r', 'a', 'n', 'z', 'e', 's']

my_string = ''.join([i for i in my_string]) # In deze stap worden de letters weer samengevoeg. Met join(). Nu kan je beginnen met veranderen toe te passen. 
print(my_string)
# output HelloMyNameIsSybeFranzes

my_string = ''.join(
    [ i if i.islower() else ' ' + i for i in my_string ]
    )

print(my_string)
# output  Hello My Name Is Sybe Franzes

# Er is ook nog een mogelijkheid om een index toe te voegen. 

my_string = ''.join(
    [ i if i.islower() else ' ' + i for i in my_string ]
    )[1:]                                                      # [1:] Hier wordt de spatie verwijderd door middel van slicen. 
print (my_string)

# +=----------------------------------------------------------------------------------------------------------------------------- if statement in List Comphrension

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

# Voorbeeld zonder list comprehesion. 

movie_name = []                     # Je begint met het aanmaken van een lege lijst. 
for title in movies:                # Loop je over de lijst heen. 
     if title.startswith('C'):      # Met het if maak je een statement. .startwith() is een built in function in Python. 
          movie_name.append(title)  # Dan voeg je het statement toe aan de lege lijst. 

print (movie_name)

# The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.

# Nu in list comphrehenion. 
# Wat we hierin willen hebben is de title (andere naam voor de i in de for loop). Dat is waar je mee begint in de comphrehension.
# Dus:  movie_name2 = [list]
# Daarna wil je een loop maken over je lijst: [for list in movies]
# Je krijgt dan: movie_name2 = [list for list in movies]
# Daarna stel je de vergelijking op die je wil hebben met je if statement. 
# Je wil de 


movie_name2 = [list for list in movies if list.startswith('C')]

print (movie_name2)

movies_date = [
("The Towering Inferno", 1970),
("Jaws", 1979), 
("Midway", 1989), 
("Star Wars", 1991), 
("Close Encounters of the Third Kind 1", 1988),
("Close Encounters of the Third Kind 2", 1986),
("Close Encounters of the Third Kind 3", 1990),
("Superman", 1991),
("Indiana Jones", 1992), 
("E.T.", 1993), 
("I.T.", 1994), 
("U.T.", 1995), 
("Y.T.", 1996), 
("O.T.", 1997), 
("Born on the Fourth of July", 1998),
("Always", 1999),
("Presumed Innocent", 1970),
("Memoirs of a Geisha", 1971)
]

# Opdracht vind alle films van voor het jaar 1990
# Note de lijst is gevschreven in tuples. Een container die specifieke informatie bevat over de film. 

pre_1990_movies = [title for (title, year) in movies_date if year < 1990]

print (pre_1990_movies)


# het jaar was niet in de lijst ingevoerd. Maar hoe kan je dit dan voor elkaar krijgen. 
# Laten we kijken naar een wiskundig voorbeeld. 

# We hebben een lijst. 

v = [2, -3, 1]

# Elk nummer willen we vermenigvuldigen met 4. 
# Wanneer je 4*v doet zal hij 4x de lijst uitprinten dat wil je niet. 
# Dus 4*v = v + v + v + v
# Je vormt dan een lijst met 4 copies van v [2, -3, 1, 2, -3, 1, 2, -3, 1, 2, -3, 1]
# Wil je elk compenent met 4 vermenigvuldigen schrijf dan deze list compheresion. 

w = [4*x for x in v]

print(w)                # output = [8, -12, 4]

