# Tuple is an heterogeneous and immutable collection
tupleEx = (1, 2, 3,)  # The syntax is similar to a list but we use parenthesis rather than square brackets
print(type(tupleEx))
oneElementTupleIncorrect = (2)  # This will result in a int type, rather than a tuple type, this not what we want
print(type(oneElementTupleIncorrect))  # This is an int not a tuple
oneElementTupleCorrect = (2,)  # We need to use trailing comma in order to make the type tuple
print(type(oneElementTupleCorrect))
emptyTuple = ()
print(type(emptyTuple))

# We can concatenate tuples

tupleOne = (1, 2, 3)
tupleTwo = (4, 5, 6)

print(tupleOne + tupleTwo)

# We can have nested tuples and access them through it index and nested index like a multidimentional array like
tupleNested = ((1, 2, 3), (10, 12, 13), (20, 21, 22))
# We can acces with the index and subindex
print(tupleNested[2][2])  # This will refers to the 2nd index set of parenthesis and the second element of that set

# We can declare ommiting the parenthesis
tuple_without_parenthesis = 1, 2, 3, 4,
print(type(tuple_without_parenthesis))

# We can deconstruct the collection like in javascript, here we need to put a variable for each index for example
(first_word, second_word, third_word) = (1, 2, 3,)
print(first_word)  # This will get the 1 value
print(second_word)  # This will get the 2 value
print(third_word)  # This will get the 3 value


# We can deconstruct the result of a reducing operation
# Consider we have a requirement of get the min and max of a tuple, it will return us two values, so we reduce the tuple
def get_min_max(x):
    return min(x), max(x)


tuple_min_max = 11, 2, 3, 12, 5543, 12, 0
lower, upper = get_min_max(tuple_min_max)
print("Lower: ", lower)
print("Upper: ", upper)

# If we want to deconstruct a different collection as a tuple,can use the tuple() constructor, which receives a iterable
str_is_iterable = "Jesus"
str_iterable_as_tuple = tuple(str_is_iterable)
print(str_iterable_as_tuple)
