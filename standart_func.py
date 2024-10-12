'''A subsidary file for writing code'''

def print_stuff():
    '''Prints smthing'''
    print("This is stuff")


def print_what_i_want(x):
    '''Function with parameter'''
    print(f"{x}")

def do_addition(x = 0, y = 0):
    '''This function calculates a sum'''
    print(f"This is a sum of {x} and {y}, which is {x + y}")
    return x + y

# Задает ТИП параметров в функции
# это немного бесполезно, ибо комипилятору плевать

def do_multiplication(x: float, y: float):
    '''This functions performs multiplication'''
    print(f"{x} * {y} = {x*y}")
    return x * y

def do_division(x, y):
    '''This functon performs division'''
    print(f'{x} / {y} = {x/y}')
    return x / y
