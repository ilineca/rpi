'''
def methodinception(another, arg1, arg2):
    return another(arg1, arg2)

def add_two_nums(arg1, arg2):
    return arg1  + arg2

print(methodinception(add_two_nums, 6, 9))


my_list = [12, 56, 454, 67]

print(list(filter(lambda x: x!= 12, my_list)))

print((lambda x: x * 3)(53))

def not_12(x):
    return x != 12



print(list(filter(not_12, my_list)))
'''
import functools
def decorator_with_args(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_wrapper_function(*args, **kwargs):
            print("in the my_decorator {} is the number ".format(number))
            func(*args, **kwargs)
            print("after the decorator")
        return function_wrapper_function
    return my_decorator


@decorator_with_args(34)
def my_function(arg1, arg2):
    print("this {} is the finction {}".format(arg1, arg2))


my_function(2, 3)
