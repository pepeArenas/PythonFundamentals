names = ['jesus', 'jose', 'miguel', 'elena', 'guadalupe']

names_iter = iter(names)

print(names_iter.__next__())
print(names_iter.__next__())
print(names_iter.__next__())
print(names_iter.__next__())
print(names_iter.__next__())
#  This will result in a StopIteration exception, when we hit the last element
print(names_iter.__next__())
