if True:
    print("Is True")

# The next print will not execute because is false
if False:
    print("Is False")

x = 10

# We can nested if inside ifs but we can use elif and it stand for the zen principle Flat is better than nested
if x > 10:
    print("Is greater than 10")
elif x < 10:
    print("Is lower than 10")
else:
    print("Is equal to 10")
