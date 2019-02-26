# This is a list with one element and the reference of its values will be repeted 5 times, so it will result in an
# array of 5 elements all of them pointing to the same references an values
s = [[1, 2, 3] * 5]

#      s
# [0][1][2][3][4]

#    0 1 2

#    1 2 3

print(s)

#  Again if we use append it will mutate the list and all of the object reference by will be updates

s[0].append(7)
print(s)

#  But if we assign an index to a new array, it will only update that index

s[0][0] = [4, 5, 6]
print(s)
