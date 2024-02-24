# Question:
# The provided code defines a function isPrime(x) that returns True if x is prime.

# Your task is to create a generator function named primeGenerator() that takes two numbers as arguments.
# This generator function should utilize the isPrime() function to yield the prime numbers within the specified range (between the two arguments).

# Sample Input:
# 10
# 20

# Sample Output:
# [11, 13, 17, 19]

# Explanation:
# The provided code takes two arguments as input and passes them to the generator function,
# then outputs the result as a list.
# Solution:

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def primeGenerator(a, b):
    i = a

    while i < b:
        if isPrime(i):
            yield i
        i += 1


f = int(input())
t = int(input())

print(list(primeGenerator(f, t)))
