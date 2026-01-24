def main():
    # sets the amount dues
    amount_due = 50

    # in a while loop till the amount is greater than 0
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        user_coin = int(input("Insert Coin: "))

        # check the user input against valid denomination
        if user_coin in [5, 10, 25]:
            # if user input valid then sub from amount due
            amount_due -= user_coin

    change_owe = abs(amount_due)
    print(f"Change Owed: {change_owe}")




main()