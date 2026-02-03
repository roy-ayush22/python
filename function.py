import math

def isPrime(n):
    if n <= 1:
        print(f"{n} is not prime")
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                print(f"{n} is not prime")
                return False
        print(f"{n} is prime")
        return True


isPrime(8)