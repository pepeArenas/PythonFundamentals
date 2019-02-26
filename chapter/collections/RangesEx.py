# Range is a type of collection in python, we can use with one, two or three parameters

#  This is just for indicating the stop point, in this case 5 which is exclusive
for i in range(5):
    print(i)
print("------------")
#  This is for indicating the starting and the stopping point, in this case 1(inclusive) and 5(exclusive)
for i in range(1, 5):
    print(i)
print("------------")
#  This is for indicating the starting, stopping and the steps in we will iterate
#  in this case 0 starting inclusive, 10 stopping exclusive and will jump 2 by 2 until stopping point
for i in range(0, 10, 2):
    print(i)

#  Also we can generate list by range using the list constructor
list_non_consecutive = list(range(1, 10, 2))
print(list_non_consecutive)

#  Always prefer the for each in order to iterate a iterable, rather than the old for way

numbers = list(range(10))
for number in numbers:
    print(number)
# Do not prefer this
print("----------")
#  Rather than this
i = 0
for i in range(len(numbers)):
    print(numbers[i])
# If we want an index we can use enumerate rather than range, this will give us a index by default
for i in enumerate(numbers):
    print(i)

# If we want to extract that index we can deconstruct the result

for index, value in enumerate(numbers):
    print("The index is {} and the value is: {}".format(index, value))
