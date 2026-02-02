def main():
    percentage = get_fuel()

    if percentage <= 1:
        print("E")
    elif percentage >= 100:
        print("F")
    else:
        print(f"{percentage}%")
    

def get_fuel():
    while True:
        try:
            fuel_fraction = input("Fraction: ")
            x,y = fuel_fraction.split("/")
            x,y = int(x), int(y)

            if x >= 0 and x <= y and y != 0:
                return round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()