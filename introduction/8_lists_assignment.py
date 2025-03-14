"""
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
"""

zoo = ["elefante", "jirafa", "mono", "pinguino", "aguila"]
print(zoo)

zoo.pop(2)
print(zoo)

zoo.append("cocodrilo")
print(zoo)

zoo.pop(0)
print(zoo)

print(zoo)
print(zoo[0:3])