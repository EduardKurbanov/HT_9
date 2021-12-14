from database import get_user_balance


def check_balance(username: str) -> object:
    money = get_user_balance(str(username))
    print("Balance: {0} USD".format(money))
