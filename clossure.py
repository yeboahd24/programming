# Decorators

def outer_function():
    message = 'HI'

    def inner_function():
        print(message)
    return inner_function()

outer_function()


# This one takes in arguments
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hey')
bye_func = outer_function('Bye')

hi_func()
bye_func()



#NB it can be like....
# def outer_function(msg)
#def inner_function()
# print(msg)
# return inner_function()
