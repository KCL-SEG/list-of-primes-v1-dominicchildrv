"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 1
    currentNumber = 2
    while count < (number_of_primes) + 1:
        isPrime = True
        for i in range (2,currentNumber + 1):
            if i == currentNumber:
                pass
            else:
                if currentNumber%i == 0:
                    isPrime = False
        if isPrime == True:
            count = count + 1
            list.append(currentNumber)
            currentNumber = currentNumber + 1

        else:
            currentNumber = currentNumber + 1


    return list

