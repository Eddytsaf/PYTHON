people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house":"Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

#people.sort(key=f)  # python does not sort a dictionnary, it sends you an error
# Another way to sort that using a lambda method
people.sort(key=lambda house: house["house"])
print(people)