"""
Sets y Tuplas
"""

print(f"\nSets")

# Definición de un Set
my_set = {5, 5, 7, 29, 36}
print(my_set)

my_set.add(39)      # add agrega un nuevo valor
my_set.discard(5)   # discard remueve un valor sin dar error

print(my_set)       # {36, 39, 7, 29}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)    # Unión: {1, 2, 3, 4, 5}
print(set_a & set_b)    # Intersección: {3}
print(set_a - set_b)    # Diferencia: {1, 2}
print(set_a ^ set_b)    # Dif Simetrica: {1, 2, 4, 5}

print(f"\nTuplas")
person = ("Kevin", 31, "Engineer")
print(person)           # ('Kevin', 31, 'Engineer')
print(person[0])        # Kevin