from collections import Counter
from database import get_available_currency, update_available_currency, get_user_balance, set_user_balance, set_user_transaction


def get_currency(money: int):
    requested_amount: int = money
    temp_list: list = []
    available_currency: dict = {}
    summ_value: int = 0

    if int(str(money)[-1]) != 0:
        print("<value is not short 10>")
        return False

    available_currency: dict = get_available_currency()

    if int(requested_amount) > 0:
        while int(requested_amount) > 0:
            for nominal, amount in available_currency.items():
                if int(amount) > 0:
                    tmp_val: int = int(requested_amount) % int(nominal)
                    if tmp_val == 0:
                        requested_amount -= int(nominal)
                        temp_list.append(nominal)
                        available_currency[nominal] -= 1
                    else:
                        continue
                else:
                    if int(amount) == 0:
                        for i in range(0, len(str(requested_amount))):
                            temp0: list = []
                            temp1: list = []
                            temp3: list = []
                            temp4: list = []
                            for nominal0, amount0 in available_currency.items():
                                pow_coefficient: int = int(len(str(requested_amount))) - (i + 1)
                                check_value: int = int(str(requested_amount)[i]) * (10 ** pow_coefficient)
                                if (check_value >= int(nominal0)) and int(amount0) > 0:
                                    amount_needed = int((check_value / int(nominal0)))
                                    if amount_needed <= int(amount0):
                                        temp0.append(int(nominal0))
                                        temp1.append(int(amount_needed))
                                        max_val = max(temp0)
                                        temp_dict: dict = dict(zip(temp0, temp1))
                                        for j in range(0, amount_needed):
                                            temp_list.append(nominal0)
                                            temp_money_value = available_currency[int(nominal0)]
                                            if temp_money_value > 0:
                                                available_currency[int(nominal0)] -= 1
                                            else:
                                                break
                                        for items, value in temp_dict.items():
                                            if (items * value) == check_value:
                                                pass
                                            elif check_value > items:
                                                for val, am in available_currency.items():
                                                    amount_needed0 = int((int(check_value - items) / int(val)))
                                                    if int(am) > 0:
                                                        if (int(max_val) + (int(val) * amount_needed0)) == check_value:
                                                            temp3.append(int(val))
                                                            temp4.append(int(amount_needed0))
                                                            temp_dict0: dict = dict(zip(temp3, temp4))
                                                            for val00 in range(0, amount_needed0):
                                                                temp_list.append(val)
                                                                temp_money_value = available_currency[int(val)]
                                                                if temp_money_value > 0:
                                                                    available_currency[int(val)] -= 1
                                                                else:
                                                                    break
                                                            break
                                                        elif (items * value) == check_value:
                                                            for val00 in range(0, amount_needed0):
                                                                temp_list.append(val)
                                                                temp_money_value = available_currency[int(val)]
                                                                if temp_money_value > 0:
                                                                    available_currency[int(val)] -= 1
                                                                else:
                                                                    break
                                    break

                        for i in temp_list:
                            summ_value += int(i)

                        if summ_value == int(money):
                            requested_amount = 0
                            break
                        else:
                            print(f"<Cant withdraw requested amount: {int(money)}>")
                            return False
                    continue
                break
    else:
        print("<Entered incorrect amount>")
        return False

    print("*" * 20)
    output: dict = dict(Counter(temp_list))
    for val, num in output.items().__reversed__():
        print(f"Nominal: {val} x {num}")
    print("*" * 20)

    update_available_currency(available_currency)

    return True


def withdraw_balance(username: str):
    current_balance = get_user_balance(str(username))

    print("Balance: {0} USD".format(current_balance))  # for debug only
    entered_money = input("Enter amount : ")
    if entered_money.isdecimal():
        if (int(entered_money) != 0) and (int(entered_money) <= int(current_balance)):
            check_state: bool = get_currency(int(entered_money))

            if check_state:
                new_balance = int(current_balance) - int(entered_money)
                print("Balance: {0} USD".format(new_balance))

                set_user_balance(str(username), int(new_balance))
                set_user_transaction(str(username), int(current_balance), int(new_balance))
            else:
                print("<Operation unsuccessful>")
        else:
            print("<Entered incorrect amount>")
    else:
        print("<Only digits allowed to enter>")
