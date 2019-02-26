# int is an unlimited precision signed integer
# We can specified as digits
digit = 10
print(digit)
# Also we can specified as binary
binary = 0b10
print(binary)
# Also we can specified as octal
octal = 0o10
print(octal)
# Also we can specified as hexadecimal
hexadecimal = 0x10
print(hexadecimal)
# When we want to transform a float to a int always is going round thought zero
print(int(3.6))  # Will go to zero so it will round to 3
print(int(-3.9))  # Will go to zero so it will round to -3
print(int("3456"))  # This will result in a number 3456
print(int("10000", 3))  # We can use optional base in this case 3 to convert to a number the passed stringx
