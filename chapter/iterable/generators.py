def odd_numbers_with_generators():
    count = 0
    while True:
        if (count % 2 == 0):
            yield count
        count += 1


prime_gen = odd_numbers_with_generators()
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))
print(next(prime_gen))
print()
print(prime_gen.__next__())
print()


#  We can have as many yields as we want to in order to return , when we pop them out it will with all the logic
#  between each yield
def gen123():
    print('Generation one')
    yield 1
    print('Generation two')
    yield 2
    print('Generation three')
    yield 3
    print('After finish yielding')


generator = gen123()
print(next(generator))
print(next(generator))
print(next(generator))


#  Generators can are stateful
#  This will return the fist three elements of a given iterable
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinc(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinc():
    items = [5, 7, 7, 6, 5, 5]
    for items in distinc(items):
        print(items)


#  In this case we are form a pipeline of the two function, take and distinct
def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for items in take(3, distinc(items)):
        print(items)


if __name__ == '__main__':
    # run_take()
    # run_distinc()
    run_pipeline()

print()
print((sum(x * x for x in range(1, 10))))
