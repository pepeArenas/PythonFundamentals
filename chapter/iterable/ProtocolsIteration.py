iterable_protocol = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator_protocol = iter(iterable_protocol)
print(next(iterator_protocol))
print(next(iterator_protocol))
print(next(iterator_protocol))
print(next(iterator_protocol))
#  In this case will throw an exception because we got to the end of the iterable, this is because we can have infinite
#  iterators, the exception that is thrown is a StopException
print(next(iterator_protocol))
