# As the zen of python quotes "Explicit is better than explicit" let see an example


x = 5
# In this case the condition is explicitly stated as x is not zero
while x != 0:
    print(x)
    x -= 1

print("-------------")
# In the next case we take advantage of the falsy property of condition on python and as 0 is false we can write
# the following code but as it imply implicit representation is not the best solution in python
c = 5
while c:
    print(c)
    c -= 1
