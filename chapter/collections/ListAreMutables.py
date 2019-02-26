lista = [1, 2, 3, 4, 5, 6, ]

start_is_inclusive = 1
stop_is_non_inclusive = -1

# We can slice with the start and the stop
slice_with_start_and_stop = lista[start_is_inclusive:stop_is_non_inclusive]

print(slice_with_start_and_stop)

slice_with_start_and_stop[1] = slice_with_start_and_stop[1] * 10

print(slice_with_start_and_stop)
print(lista)

# We can slice just with the start and omiting the stop will bring us from start to the end

slice_with_start_only = lista[2:]
print(slice_with_start_only)  # Here we got from index 2 to the end

# We can slice just with the stop and ommiting the start, this will bring us from the index 0 to the non inclusive stop

slice_with_stop_only = lista[:3]
print(slice_with_stop_only)  # In this case it will bring us from the beginning to non inclusive 3 element mean index 2

# Also we can access to the index with negative index, so we have the following
# Positive index  0,     1,      2,      3,      4
# Values          1,     2,      3,      4,      5
# Negative index  0     -4       -3     -2      -1
# We can access from negative indexes and is like starting from the right to left
print("+" * len(lista))
print(lista)
print("+" * len(lista))

slice_from_right_to_left = lista[-4:-1]
print(slice_from_right_to_left)  # In this case we access from inclusive -4  to non inclusive -1

# We can have a full slice meaning a copy with [:]

full_slice = lista[:]
print(id(lista))
print(lista)
print(id(full_slice))
print(full_slice)

# Both list are different in identity
print(lista is full_slice)  # Means is another reference
# But same as values
print(lista == full_slice)  # Means the values are the same

# Other ways to copy a list, although we need to keep in mind that the copies are shalow copies
u = lista.copy()
x = list(lista)  # This is preferred because with the constructor we can have any iterable copied
