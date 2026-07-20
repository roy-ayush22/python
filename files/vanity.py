def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6) or not s.isalnum():
        return False
    
    if not s[:2].isalpha():
        return False
   
    found_digit = False
    for char in s:
        if char.isdigit():
            if not found_digit and char == '0':
                return False
            found_digit = True
        elif found_digit:
            return False
    
    return True

main()