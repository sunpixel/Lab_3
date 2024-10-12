'''This code file contains functions with KWARGS and ARGS'''

def arg_function(*args):
    '''Will print all args'''
    for i in args:
        print("---------")
        print(i)
        print("---------")

def kwrarg_function(**kwargs):
    '''This function will unpack all the KWARGS packed in it'''
    print(kwargs)

def unpack_args_1(*args):
    '''This function will unpack'''
    result = 0
    for num in args:
        result += num
    print(f"The result is {result}")

def unpack_args_2(name, fname, middlename):
    '''This function will unpack all arguments when passed'''
    print(f"{fname} {name} {middlename}")

def unpack_kwargs(name, age, position):
    '''This function unpacks all data baes on keyword data'''
    print(f"Name:{name}, Age: {age}, Position: {position}")
