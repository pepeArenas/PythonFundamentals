count = 0


def show_count():
    print("count = ", count)


def set_count(c):
    count = c


show_count()  # Will print the global count 0
# This will not take effect because count is assigned in the local scope so the 5 will live just
# by the end of the function
set_count(5)

show_count()  # Will print the global count 0


# In order to modify the global variable from a function scope we need to prefix the variable with the global keyword

def override_global_count(c):
    global count
    count = c


override_global_count(5)
show_count()  # This will have the 5 value
