#  String is an immutable and homogeneous sequence of characters

name = "Jose"
#  We can concatenate with the + symbol although is not to performance friendly
name += " de Jesus"  # In this case we are creating a temp reference and this is a new string
#  Prefer use the method join that is kind of a builderString with java, is better with performance
joinName = ";".join(["jose", "de", "jesus"])  # This will create a string separate by ;
print(joinName)

joinNameEmpty = "".join(["Jose", " ", "de", " ", "Jesus"])  # This is the preferred way of concatenate several string
#  With an empty string and join the words
print(joinNameEmpty)

#  Also we can deconstruct the join by assign to a variables with split()

print(joinNameEmpty.split(" "))  # We are splitting by empty space

#  With partition we can have a three part array, one for separator and two for the left and right from separator

print(joinNameEmpty.partition("de"))  # This will result in [Jose][de][Jesus]

#  With format we can access to any atribute of an object
print("Jose de {} has {}".format("Jesus", 34))  # In this case we ommit the index because it will respect the order

tupleEx = ((1, 2), (3, 4), (5, 6))
print("Jose {0}".format(tupleEx[1][1]))
print(f"Jose {tupleEx[1][1]}")

# The common practice with partition is underscore as partition name
left, _, right = "Jose de Jesus".partition("de")
print(left)
print(_)  # This contains the separator and the underscore is the common practice to name the separator
print(right)
