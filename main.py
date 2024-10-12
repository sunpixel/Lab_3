'''Here will be imported stuff and functions'''
import standart_func as sf
import complex_functions as cf
import args_and_kwargs as argakwarga

def show_result():
    '''Shows result'''
    string = "-"
    #
    # Block 1
    sf.print_stuff()
    sf.do_addition(1, 5)
    sf.do_multiplication(12, 6)
    sf.do_division(4, 10)
    print(string * 20)

    # Block 2
    numbers = [1, 4, 6, 8, 12, 7, 90]
    smth = {'name': 'Sun', 'age': '21', 'position': 'employee'}
    user = ('Username', 'Password', 'email')

    argakwarga.arg_function(numbers)
    argakwarga.kwrarg_function(name='Nikita', lang='Python')
    argakwarga.unpack_args_1(*numbers)
    argakwarga.unpack_args_2(*user)
    argakwarga.unpack_kwargs(**smth)
    print(string * 20)

    # Block 3
    cf.do_smth()
    cf.complex_1(6, 8, sf.do_addition)
    cf.complex_2(sf.do_multiplication)
    cf.complex_3(sf.print_stuff)
    cf.local_func_1()
    cf.local_func_2()
    print(string * 20)

    # Block 4

    func1 = lambda: print("This is lambda function")
    func2 = lambda a, b, operation: print(f'{operation(a, b)}')

    func1()
    func2(12, 44, sf.do_multiplication)
    cf.aws_function(lambda a, b: a + b, 10, 4)
    #
    print(string * 20)
    fn = cf.multiply(6)
    print(fn(7))
    print(fn(8))

    fun = cf.used_times(10)
    print(fun(2))
    print(fun(6))

    dumb = lambda a: lambda b: a / b

    new = dumb(123)
    print(new(4))
    print(new(12))


if __name__ == '__main__':
    show_result()
