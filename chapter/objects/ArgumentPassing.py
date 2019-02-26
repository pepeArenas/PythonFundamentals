# Arguments are passing by reference not by value, so a function will receive a reference to the argument itself
# and if is not reasign the entire object to a new memory location, the reference will not change
# When we have x =[1,2,3] this is reasign the entire object if we assign a index x[1]=10 this not change reference
# The complete reasign will change reference

x = [1, 2, 3]


# Here we will receive a reference of the passed object and as soon we do not reasign it will be the same object
def changeByIndexWillNotGiveUsANewReference(y):
    y[1] = 10
    print('y=', y)
    return y


y = changeByIndexWillNotGiveUsANewReference(x)

print('x=', x)

# There are the pointing to the same memory location
print(x is y)

# If we want to change the reference we need to reasign inside the method the argument that is passed
p = [1, 2, 3]


def reassignWillGiveUsANewInstance(r):
    r = [0, 9, 8]
    print('r=', r)
    return r


r = reassignWillGiveUsANewInstance(p)

print('p=', p)
print('r=', r)
print('p is r', p is r)


# As we can see the return keyword will return the same reference if we don't reassign otherwise will do

# We can use positional arguments, this ones are the nornal args that match by position example
def withPositionalArgs(param1, param2):
    print(f"Param1: {param1} param2: {param2}")


# When we call the function we pass the parameters in the order in which we define the list of arguments in the method
withPositionalArgs(2, 4)


# There is something called keyword arguments, in this case is no matter the order because we send them as part of the
# client call, so is responsible of the client to add the pair of name and value in the call
def withKeywordArgs(name, age):
    print(f"Name: {name} age: {age}")


# Then when we call we need to specify the names of the params and its values, an no matter the order
withKeywordArgs(age=23, name="Jesus")


# If we want to use positionals and keyword arguments together, we need to put the keyword at the last
def with_both_types_of_args(name, age):
    print(f"Name 2: {name} age 2: {age}")


# withBothTypesOfArgs(age=23, "Jose") This line is not allowed, it must be the keyword args place at the end

# with_both_types_of_args(23, name="Jesus")


# We can use default values
def with_default_arg_values(name, separator="*"):
    line = separator * len(name)
    print(line)
    print(name)
    print(line)


with_default_arg_values("Jesus")

# If we want to override the default separator we send it when we call
with_default_arg_values("Mondragon", "-")

import time


def show_default(arg=time.ctime()):
    print(arg)


# The default values are just evaluated one type and is when the function is evaluated, so if we execute the method
# several times, we will get the same timestamp as the first one, because is will be like a constant value because is
# just one time evaluated
show_default()
show_default()
show_default()
show_default()
show_default()


def add_spam(menu=[]):
    menu.append("spam")
    return menu


breakfast = ["bacon", "eggs"]

print(add_spam(breakfast))

lunch = ["backed beans"]

print(add_spam(lunch))

# If we just try to use the default argument of the add_spam method we have the following behaviour
print(add_spam())  # [spam]
print(add_spam())  # [spam, spam]
print(add_spam())  # [spam, spam, spam]

# The default method when is a list default, as mention before the default values are just created once the function
# is evaluated, that is the reason that it will be append to the same list and it will grow
print("--------------")


# The solution is use immutable objects as default arguments
def add_spam_immutable(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


print(add_spam_immutable())  # [spam]
print(add_spam_immutable())  # [spam]
print(add_spam_immutable())  # [spam]
