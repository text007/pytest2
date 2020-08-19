
def a_new_decorator(a_func):

    def wrapthefunction():
        print("i am doing some bork before execution a_func()")

        a_func()

        print("i am doing some boring work after executing a_func()")

    return wrapthefunction


@a_new_decorator
def a_function_requiring_decoration():
    print("i am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
