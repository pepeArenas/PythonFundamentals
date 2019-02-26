numbers = [[1, 2, 3], [4, 5, 6]]
ages = numbers[:]

print("Both list: numbers and ages has the same values", numbers == ages)
print("Both list: numbers and ages has not the same identity", numbers is ages)

print(
    "If we reassign ages[0] it will make a new reference for that index and it will be "
    "independent from the numbers list")

ages[0] = [7, 8, 9]
print(ages[0])  # This has the new value that we just reassign
print(numbers[0])  # This has the same value as the beginning, and do not have any reference to ages[0]

print("Buf if we just append to a ages[1], this is a mutable operation this  will change both list because"
      "we are not reassign anything ")

ages[1].append(34)

# The following lines has the same values
print(ages[1])
print(numbers[1])
