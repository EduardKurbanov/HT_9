import sqlite3


class LoginException(Exception):
    pass


class PasswordException(Exception):
    pass


def verification_password_login(username="", password="", special_key=""):
    try:
        con = sqlite3.connect("bank_db.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM users_pass WHERE login LIKE \"%{username}%\";")
        login_db = cursor.fetchall()[0][1]
        cursor.execute(f"SELECT * FROM users_pass WHERE login LIKE \"%{username}%\";")
        password_db = cursor.fetchall()[0][2:]
        con.commit()
        con.close()

        if username == login_db:
            if (password, None) == password_db:
                return True
            elif (password, special_key) == password_db:
                return "incasation"
            else:
                raise PasswordException(f"<incorrect password -> {password}>")
        else:
            raise LoginException(f"<incorrect login -> {username}>")
    except LoginException as err:
        print(f"<status incorrect login -> {err}>")
    except PasswordException as err:
        print(f"<status incorrect password -> {err}>")
