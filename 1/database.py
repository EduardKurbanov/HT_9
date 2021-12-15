import sqlite3 as database
import time

db_dump = database.connect("bank_db.db")


def close_database():
    db_dump.close()


def get_user_data_from_db(user_name: str):
    temp_db_list: list = []
    cur = db_dump.cursor()
    cur.execute(f"SELECT * FROM users_pass WHERE login LIKE \"%{user_name}%\"")
    cursor = cur.fetchall()
    for data in cursor:
        temp_db_list.append(data[0])
        temp_db_list.append(data[1])
        temp_db_list.append(data[2])
        temp_db_list.append(data[3])

    return temp_db_list


def get_user_balance(user_name: str):
    user_id: str = None
    user_balance: str = None
    cur = db_dump.cursor()
    cur.execute(f"SELECT id FROM users_pass WHERE login LIKE \"%{user_name}%\"")
    cursor = cur.fetchall()
    for data in cursor:
        user_id = data[0]

    cur.execute(f"SELECT amount FROM balance WHERE id LIKE \"%{user_id}%\"")
    for data in cur:
        user_balance = data[0]

    if user_balance is None:
        return int(0)
    else:
        return int(user_balance)


def set_user_balance(user_name: str, money_amount: int):
    if money_amount > 0:
        user_id: str = None
        cur = db_dump.cursor()
        cur.execute(f"SELECT id FROM users_pass WHERE login LIKE \"%{user_name}%\"")
        cursor = cur.fetchall()
        for data in cursor:
            user_id = data[0]

        cur.execute(f"UPDATE balance SET amount = {money_amount} WHERE id = {user_id}")
        db_dump.commit()
    else:
        print("<Money amount cant be negative>")


def set_user_transaction(user_name: str, old_balance: int, new_balance: int):
    if old_balance > 0 and new_balance > 0:
        user_id: str = None
        operation_type: str = None
        cur = db_dump.cursor()
        cur.execute(f"SELECT id FROM users_pass WHERE login LIKE \"%{user_name}%\"")
        cursor = cur.fetchall()
        for data in cursor:
            user_id = data[0]

        if old_balance > new_balance:
            operation_type = "Withdraw"
        elif new_balance > old_balance:
            operation_type = "refill"
        else:
            operation_type = "no changes"

        cur.execute(f"INSERT INTO transactions (user_id, old_balance, new_balance, op_type, stamp) "
                    f"VALUES ({int(user_id)}, {int(old_balance)}, {int(new_balance)}, '{str(operation_type)}', {int(time.time())})")
        db_dump.commit()
    else:
        print("Error")


def get_available_currency():
    cur = db_dump.cursor()
    cur.execute(f"SELECT * FROM atm_available_money")
    cursor = cur.fetchall()
    return dict(cursor)


def update_available_currency(available_curr_list: dict):
    cur = db_dump.cursor()

    for cur_id, cur_amount in available_curr_list.items():
        cur.execute(f"UPDATE atm_available_money SET money_amount = {cur_amount} WHERE money_id = {cur_id}")
        db_dump.commit()

