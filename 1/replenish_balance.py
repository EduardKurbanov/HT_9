from database import get_user_balance, set_user_balance, set_user_transaction


def replenish_balance(username: str):
    current_balance = get_user_balance(str(username))

    print("Balance: {0} USD".format(current_balance))  # for debug only
    entered_money = input("Enter amount : ")
    if entered_money.isdecimal():
        if int(entered_money) != 0:
            new_balance = int(current_balance) + int(entered_money)
            print("Balance: {0} USD".format(new_balance))

            set_user_balance(str(username), int(new_balance))
            set_user_transaction(str(username), int(current_balance), int(new_balance))
        else:
            print("Entered incorrect amount")
    else:
        print("Only digits allowed to enter")
