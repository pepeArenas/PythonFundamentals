#  In situ modification by sort or reversed

namesMutableSortReverse = ["Jesus", "Jose", "Guadalupe", "Miguel"]
print("Original list", namesMutableSortReverse)
namesMutableSortReverse.sort(key=len, reverse=True)
print("We are modifing the same list", namesMutableSortReverse)
namesMutableSortReverse.reverse()
print("We are modifing the same list", namesMutableSortReverse)
print()

#  Not in situ modification by sort or reversed
namesTwo = ["Jesus", "Jose", "Guadalupe", "Miguel"]
print()
print("Original list", namesTwo)
print("This will show the list reversed, but it will not modify the original list, will t"
      "return a iterator thats why we need to convert by using list constructor", list(reversed(namesTwo)))
print("As we can see we still have the original list untouch ", namesTwo)
print()
print("We also can sorted by it lenght, this returns a list", sorted(namesTwo, key=len))
print("As we can see we still have the original list un touch", namesTwo)

name = "Jesus"
age = 34
last_name = 'Arenas'

print('The resume', '\n\tName:', name, '\n\tLast Name:', last_name, '\n\tAge:', age)
