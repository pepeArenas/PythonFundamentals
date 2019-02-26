# Python has DYNAMIC and STRONG type system, that means the following


# It is said that it is DYNAMIC if we do not define a specific type then we declare the object
def dynamic_args_example(arg1, arg2):
    print(f"The result of {arg1} + {arg2} is {arg1 + arg2}")


# And we can send whatever type we want for example
# A couple of integers
dynamic_args_example(1, 2)
# A couple of strings
dynamic_args_example("jose ", "de jesus")
# A couple of list
dynamic_args_example([1, 2, 3, ], [3, 2, 1, ])

# It is said that is a STRONG typed system when the language generally do not convert implicitly for example
# a String and a integer
# dynamic_args_example("1", 3)  This will result in a TypeError
# a array and a integer
# dynamic_args_example([1,2], 3)  This will result in a TypeError

# So no matter if we can send whatever type to a function and the function will try to resolve,but if we mix the types
# it will not convert explicitly
