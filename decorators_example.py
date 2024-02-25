# You are working on an invoicing system.
# You need to add a decorator for the invoice() function, that will print the invoice in the following format:
# Sample Input: 42
# Sample Output:
# ***
# INVOICE #42
# ***
# END OF PAGE

# Decorator function
def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")

    return wrap

# Function decorated with the `decor` decorator
@decor
def invoice(num):
    print("INVOICE #" + num)

# Calling the decorated function
invoice(input())
