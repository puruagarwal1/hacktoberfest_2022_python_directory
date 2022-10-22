def factorial(fact):
    if fact == 0 or fact == 1:
        return 1
    return fact*factorial(fact-1)

x=int(input('Enter a number: '))
print(factorial(x))