# Def functions

def double(x):              # Een functie start altijd met def. Double is hierin de functie naam. Tussen haakjes staat de input variabele. 
    doubled_x = x * 2       # Op de tweede lijn komt te staan wat de functie moet doen. 
    return doubled_x        # Dit bevestigd de functie en geeft double_x weer terug. 

four_doubled = double(4)
print(four_doubled)

# The Python return statement is a special statement that you can use inside
# a function or method to send the function's result back to the caller. 
# A return statement consists of the return keyword followed by an optional return value. 
# The return value of a Python function can be any Python object.
# This value is often unseen by the human user, but it can be used by the computer in further functions.
# If the return statement is without any expression, then the special value None is returned.

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()   # .find vind hier de spatie en voegt er 1 aan toe. De eerste letter van de achternaam. 
    return f'{first}. {last}.'              # Geeft terug de invoer van de opdracht. 

print (initials('Ex Ample'))
print (initials('Bob Cat'))
print (initials('Function Nice'))

def multiply(a, b):
    return a * b

print(multiply(2, 2))
print(multiply(9, 2.3))
print(multiply(29, 'Hey! '))




