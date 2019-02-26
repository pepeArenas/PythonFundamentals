#  We can search in a list by index, this will give us the index for a given value

names = ["Jose", "Jesus", "Guadalupe", "Miguel", "Miguel"]

print(names.index("Jesus"))

#  If not exist, we will get an error ValueError

# print(names.index("Elena"))

print("This line will give us the count of a given value", names.count("Miguel"))

print("In this case we are looking if a given value is in the list", "Jesus" in names)
print("In this case we are looking if a given value is in the list", "Jesus" not in names)

#  It works with any iterable

name = "Jose Jose de Jesus Arenas Mondragon"

print("In this case we are looiking for all the o in the name", name.count("o"))
print(" " in name)
print(" " not in name)

#  For deleting we can do with index or by name or a combination of index and del
nameSeparated = "Jose Jose de Jesus Arenas Mondragon".split()

nameSeparated.remove("Jose")  # If we have two elements with the same is only remove the first

del nameSeparated[0]  # Also we can remove from a index

print(nameSeparated)

del nameSeparated[nameSeparated.index("Mondragon")]  # Or with del an the index

print(nameSeparated)

# Insert elements

nameSeparated.insert(len(nameSeparated), "Mondragon")  # We are inserting at the end
print(nameSeparated)

# For growing list

listaOne = [1, 2, 3]
listaTwo = [4, 5, 6]

listaThree = listaOne + listaTwo
print("We can use the + sign", listaThree)
listaThree += [10, 11, 12]
print("We can use +=", listaThree)
listaThree.extend([21, 22, 23])
print("We also can add elements with extend", listaThree)
