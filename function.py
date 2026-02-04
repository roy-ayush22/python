import math

def main():
    def isPrime():
        num = int(input("Number: "))
        if num <= 1 :
            print(f"{num} is not prime")
            return False
        else:
            for i in range(2, int(math.sqrt(num)) +1):
                if num % i == 0:
                    print(f"{num} is not prime")
                    return False
        print(f"{num} is prime")
        return True
    isPrime()
        
main()