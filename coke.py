def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amounr Due: {amount_due}")
        user_input = int(input("Insert Coin: "))

        if user_input in [5,10,25]:
            amount_due -= user_input
    
    amount_owed = abs(amount_due)
    print(f"Change Owed: {amount_owed}")

main()