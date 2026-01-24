name = input("what's your name? ")


match name:
    case 'harry' | 'hermione' | 'ron':
        print("griffindor")
    case 'draco':
        print("slythrin")
    case _:
        print("kon??")