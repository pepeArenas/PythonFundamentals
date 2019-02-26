from math import factorial

names = ['jesus', 'jose', 'guadalupe', 'miguel', 'elenita']

#  Here we are in a more functional style, we need to wrap all in [], in this case we are getting the length of each
#  word with len(name), name inside parenthesis is from the for and is the variable temp name for each name in the for
print([len(name) for name in names])

#  expression(item) for item in iterable]


#  The previous was the similar to the following in an imperative approach
names_length = []

for name in names:
    names_length.append(len(name))

print(names_length)

numbers = range(10)

print([(number * number) for number in numbers])

factorial_using_list = [factorial(number) for number in range(20)]
print('Factorial using list:', factorial_using_list)

# SET has the same functionality but removing the duplicates and use {} rather than []

factorial_using_set = {factorial(number) for number in range(20)}
print('Factorial using set:', factorial_using_set)

#  Here using the map as the same of set we use {}, but in order to differentiate we need to pass key value pair
country_to_capital = {'mexico': 'ciudad de mexico',
                      'brazil': 'brazilia',
                      'united kingdom': 'london'}
print('From country to capital:', country_to_capital)

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

print('From capital to country, we are switching', capital_to_country)

#  Later keys will override earlier keys, in this case it will override jesus for jose
names_first_letter = ['jesus', 'jose', 'miguel']
print({first_letter[0]: first_letter for first_letter in names_first_letter})

c = (1, 2, 3, 4, 5)

#  Filtering, we can add an if statement in order to filter while iterating
print([pow(x, 2) for x in c])

print('We can form complex structures, in this case we are creating a map with a tuple based on x',
      {x * x: (1, x, x * x) for x in range(30)})
