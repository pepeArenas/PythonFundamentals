names = {'jesus', 'miguel m', 'miguel a', 'elena', 'guadalupe a', 'guadalupe m'}
between_twenty_and_thirty = {'guadalupe m'}
between_thirty_and_forty = {'jesus', 'guadalupe a', 'miguel m'}
older_than_forty = {'elena', 'miguel a'}
pets = {'Mr pepper'}

print('This will print all the names and between_twenty_and_thirty once',
      names.union(between_twenty_and_thirty))
print('Is commutative, so it no matter the order of the operation it will not affect the result',
      between_twenty_and_thirty.union(names))

print('If we want to know the elements that are common in both list ',
      names.intersection(between_twenty_and_thirty))
print('Also is commutative and no matter the order in which we do the comparation',
      between_twenty_and_thirty.intersection(names))

print('In this case we have something similar to right outer join',
      names.difference(between_twenty_and_thirty))

print('This is not commutative, so if we change the order it will return us different set',
      between_twenty_and_thirty.difference(names))

print('Symmetric difference will give us right outer and left outer join but without the things that share each set',
      older_than_forty.symmetric_difference(names))

print('Symmetric difference is commutative will',
      names.symmetric_difference(older_than_forty))

print('In this case we are saying that all the elements of the set of the left are subset of the set of the right',
      between_thirty_and_forty.issubset(names))
print('Is not commutative, because names is not a subset of between thirty and forty',
      names.issubset(between_thirty_and_forty))
print('In this case we are saying that all the elements of the set of the left are superset of the set of the right',
      between_thirty_and_forty.issuperset(names))
print('Is not commutative, because names is not a superset of between thirty and forty',
      names.issuperset(between_thirty_and_forty))

print('In this case we are saying that names do not have any relation with the set from right which is true',
      names.isdisjoint(pets))
print('In this case we are saying that names do not have any relation with the set from right which is false',
      names.isdisjoint(older_than_forty))
