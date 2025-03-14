"""
Las listas son colecciones de data
"""

my_list = [56, 35, 27, 46, 51]

# Imprimir la lista
print(my_list)

# Imprimir un elemento especifico
print(my_list[2])

# Imprimir el tamaño de una lista
print(len(my_list))

# Imprimir un rango de números sin incluir el final
print(my_list[1:3])

# Agregar un elemeto
my_list.append(26)
print(my_list)

# Insertar un elemento en un indice
my_list.insert(2, 24)
print(my_list)

# Elimina un elemento por su valor
my_list.remove(51)
print(my_list)

# Elimina un elemento por su indice
my_list.pop(3)
print(my_list)

# Ordena la lista
my_list.sort()
print(my_list)