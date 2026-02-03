def findFactorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "undefined"
    else:
        result = 1
        for i in range(num, 0, -1):
            result = result * i
        return result
    
print(findFactorial(3))