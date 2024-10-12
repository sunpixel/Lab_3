'''This code file contains COMPLEXly structured functions'''
import random as rand

def do_smth():
    '''This function selects operation on random'''
    x = rand.randrange(0, 4)
    match x:
        case [0]:
            do_0()
        case [1]:
            do_1()
        case [2]:
            do_2()
        case [3]:
            do_3()
        case [4]:
            do_4()


def do_0():
    '''This function will perform and operation'''
    print('This is a number 0')

def do_1():
    '''This function will perform and operation'''
    print('This functions is function number 1')

def do_2():
    '''This function will perform and operation'''
    print('IDK the number of it but i guess it is 2')

def do_3():
    '''This function will perform and operation'''
    print('Deffinetly not number 4 and not number 1. I guess it is number 3')

def do_4():
    '''This function will perform and operation'''
    print('I am the greatest function number 4!!!')

def complex_1(x, y, operation):
    '''A function that has a function as its parameter'''
    print(f"Result of operation is {operation(x, y)}")

def complex_2(function):
    '''A simple function'''
    print(f"Result of random operation is {function(rand.randrange(1, 20), rand.randrange(1, 20))}")

def complex_3(non_math):
    '''This function will execute any function with no parameters'''
    print(f"The result is {non_math()}")



def local_func_1():
    '''Function will have a local subfunction'''
    def locacl_inside(a):
        '''This is a local subfunction'''
        print(a + rand.randrange(10))

    x = rand.randrange(5)
    locacl_inside(x)

def local_func_2():
    '''This function will have a local subfunction'''
    def local_inside():
        '''This is a local subfunction'''
        print("I am inside the local function")

    local_inside()


def aws_function(oprt, a, b):
    '''Performs math operations'''
    result = oprt(a, b)
    x = rand.randrange(1, 10)
    exprs = lambda a, b: a * b
    print(f"{exprs(result, x)}")


def multiply(n):
    '''A function'''
    return lambda m: n * m


def used_times(a):
    '''Function'''
    def used(b):
        '''Sub function'''
        return a + b
    return used
