"""
Перепишіть програму-банкомат на використання бази даних для збереження всих даних.

Використовувати БД sqlite3 та натівний Python.

Дока з прикладами: https://docs.python.org/3/library/sqlite3.html

Туторіал (один із): https://www.sqlitetutorial.net/sqlite-python/

Для уніфікації перевірки, в базі повинні бути 3 користувача:

  ім'я: user1, пароль: user1

  ім'я: user2, пароль: user2

  ім'я: admin, пароль: admin, special_key: admin (у цього коритувача - права інкасаторара)
"""

from verification_password_login import verification_password_login
from check_balance import check_balance
from replenish_balance import replenish_balance
from withdraw_balance import withdraw_balance
from count_currency import console_admin
from database import close_database


def start():
    count = 3
    while True:
        try:
            login = input("enter login: ")
            password = input("enter password: ")
            print("if there is no additional key press skip the step: ")
            special_key = input("enter additional key: ")
            valid = verification_password_login(login, password,special_key)
            while count > 0:
                if valid == "incasation":
                    console_admin(valid)

                if valid:
                    print("*" * 25)
                    print("1. Look at the balance")
                    print("2. Replenish the balance")  # пополнить счет
                    print("3. Withdraw cash")  # снять наличные
                    print("4. Exit")
                    print("*" * 25)
                    menu_item = input("Choose : ")
                    if int(menu_item) == 1:
                        check_balance(login)
                    elif int(menu_item) == 2:
                        replenish_balance(login)
                    elif int(menu_item) == 3:
                        withdraw_balance(login)
                    else:
                        close_database()
                        exit()
                else:
                    count -= 1
                    print(f"attempt -> {count}")
                    break

                if count > 0:
                    continue
                else:
                    print("<exit the program automatically>")
            if count == 0:
                break

        except Exception as err:
            print(f"<error -> {err}>")


# if __name__ in "__main__":
start()
