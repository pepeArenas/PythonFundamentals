def add_with_custome_message_on_exception(left, right):
    result = 0
    try:
        result = left + right
    except TypeError:
        print("We just add numbers")
    return result


def add_without_custome_message_on_exception(left, right):
    result = 0
    try:
        result = left + right
    except TypeError as err:
        print(err)
    return result


print(add_with_custome_message_on_exception(2, 3))
print(add_with_custome_message_on_exception(2, "s"))
print(add_without_custome_message_on_exception(2, 3))
print(add_without_custome_message_on_exception(2, "s"))


def open_non_existing_file(filename):
    try:
        file = open(filename, 'r')
        for line in file:
            print(line)
        file.close()
    except FileNotFoundError as err:
        print(err)


open_non_existing_file('non_existing.txt')


def raise_an_excepcion(a, b):
    if (b == 0):
        raise ValueError('No division by 0')


try:
    raise_an_excepcion(1, 0)
    print('If an exception this line will never print')
except ValueError as err:
    print(err)
finally:
    print('This will always print no matter if is ok or not')


def re_raise_exeption(a, b):
    if b == 0:
        raise ()


try:
    re_raise_exeption(1, 0)
except TypeError as err:
    print(str(err))
