# In python everything is an object, imports, modules, functions, primitive objects
from chapter.objects.ArgumentPassing import add_spam

print(dir(add_spam))  # Will give us all the object properties and methods from an object
print(type(add_spam))  # Will give us the type of the object, in this case is a function

x = 3

print(type(x))
print(dir(x))  # As we  can se it will return us the attibutes and each attibute is itself an object

print(type(x.__abs__()))
print(dir(x.__abs__()))

print(add_spam.__name__)  # Bring us the name of the object associated to the reference
print(add_spam.__doc__)  # Bring us the documentation
