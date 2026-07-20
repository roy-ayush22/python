def main():
    findFactorial()

def findFactorial():
        num = int(input("Number: "))
        if num == 1 or num == 0:
            print("Factorial: 1")
        elif num < 0:
            print("undefined")
        else:
            result = 1
            for i in range(num, 0, -1):
                result = result * i
            print(f"Factorial: {result}")

main()