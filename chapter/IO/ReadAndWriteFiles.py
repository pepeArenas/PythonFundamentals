def persist_data(data):
    #  The second parameter refers to the mode in which we are accessing to the file an if not exist it will create
    #  w is for write
    #  a is for append, this will add an not override the content of the file (if any)
    #  r is for read
    persisted = open('data.txt', 'a')
    for key, value in data.items():
        persisted.write(str(key) + ' - ' + value + '\n')

    persisted.close()


def read_data(file_name):
    #  If we want to open a file that not exist, it will throw us and exception
    returned_data = open(file_name, 'r')
    for line in returned_data:
        #  In this case we are assigning to a double variable the key value pair separating the result by spliting
        (id_product, product) = line.split(' - ')
        line.strip()
        print(id_product, product)
    returned_data.close()


products = {1: 'Hammer', 2: 'Screwdriver', 3: 'Nail'}

persist_data(products)
read_data('data.txt')
