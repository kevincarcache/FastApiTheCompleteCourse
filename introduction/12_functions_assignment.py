"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and returns a dictionary based on those values
"""

def get_person(firstname, lastname, age):
    person_item = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return person_item

print(get_person(firstname="kevin", lastname="carcache", age=31))