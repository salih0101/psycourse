import sqlite3
from datetime import datetime, timedelta

connection = sqlite3.connect('datapsycho.db')
sql = connection.cursor()


def add_user(user_id, name, phone_number, time_sub, end_sub, gender, status, amount_s):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?);',
                (user_id, name, phone_number, time_sub, end_sub, gender, status, amount_s))
    connection.commit()
    return add_user


def add_paid_user(user_id, name, phone_number, time_sub, end_sub, gender, status, amount_s):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO paid VALUES (?,?,?,?,?,?,?,?);',
                (user_id, name, phone_number, time_sub, end_sub, gender, status, amount_s))
    connection.commit()
    return add_user


def check_user(user_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT user_id, amount_sub FROM users WHERE user_id=?;', (user_id,))

    if checker.fetchone():
        return True
    else:
        return False


#Проверка оплаты пользователя
def check_pay(user_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()
    checker = sql.execute('SELECT status FROM users WHERE user_id=?;', (user_id,))

    if checker.fetchone()[0] == '1':
        return True
    else:
        return False


#Проверка подписки пользователя
def check_sub(user_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    dead = sql.execute('SELECT end_sub FROM users WHERE user_id=?;', (user_id,))
    return dead.fetchone()[0]


def get_name_all_category(current_product):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    all_products = sql.execute('SELECT * FROM tasks WHERE name=?;', (current_product, ))
    return all_products.fetchone()


def get_info_courses(category_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    categ_id = sql.execute('SELECT * FROM tasks WHERE id=?;', (category_id,))
    return categ_id.fetchall()


def get_courses():
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    category = sql.execute('SELECT * FROM tasks WHERE id=11;')
    return category.fetchall()


def change_name(user_id, name):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    sql.execute('UPDATE users SET name=? WHERE user_id=?;', (name['name'], user_id))
    connection.commit()


def change_number(user_id, phone_number):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    sql.execute('UPDATE users SET phone_number=? WHERE user_id=?;', (phone_number['phone_number'], user_id))
    connection.commit()


def deadline(user_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    dead = sql.execute('SELECT end_sub FROM users WHERE user_id=?;', (user_id,))
    result = dead.fetchone()
    if result is not None:
        return result[0]
    else:
        return None


def set_trial_sub(user_id, time_sub, end):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    time_s = sql.execute('UPDATE users SET time_sub=?, end_sub=? WHERE user_id = ?;', (time_sub, end, user_id))
    connection.commit()
    return time_s


# Платная подписка
def set_sub_end(user_id):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    current_time = datetime.now()
    exp = current_time + timedelta(days=30)

    sub = sql.execute('update users set end_sub = ? where user_id = ?;', (exp, user_id))
    connection.commit()
    return sub


def add_payment_amount(amount_sub, user_id, status):
    connection = sqlite3.connect('datapsycho.db')
    sql = connection.cursor()

    payment = sql.execute('update users set amount_sub = ?, status=? where user_id = ?;', (amount_sub, status, user_id,))
    connection.commit()
    return payment


def set_status(user_id, status):
    try:
        connection = sqlite3.connect('datapsycho.db')
        sql = connection.cursor()

        # Сначала удалим старую запись, если она существует
        sql.execute("DELETE FROM user_status WHERE user_id=?", (user_id,))

        # Теперь установим новое значение статуса
        sql.execute("INSERT INTO user_status (user_id, status) VALUES (?, ?)", (user_id, status))
        connection.commit()

    except sqlite3.Error as e:
        print(f"Ошибка при установке статуса: {e}")


def update_status(user_id):
    try:
        # Устанавливаем соединение с базой данных с помощью менеджера контекста (оператор with)
        with sqlite3.connect('datapsycho.db') as connection:
            # Создаем курсор с использованием соединения
            sql = connection.cursor()

            # Проверяем, существует ли запись с указанным user_id
            sql.execute("SELECT status FROM user_status WHERE user_id = ?", (user_id,))
            result = sql.fetchone()

            if result:
                # Если запись существует, получаем текущий статус
                current_status = result[0]
                # Вычисляем новый статус
                new_status = current_status + 1
                # Обновляем статус в таблице
                sql.execute("UPDATE user_status SET status = ? WHERE user_id = ?", (new_status, user_id))
            else:
                # Если записи нет, создаем новую с начальным статусом (например, статус 0)
                sql.execute("INSERT INTO user_status (user_id, status) VALUES (?, ?)", (user_id, 0))

            connection.commit()

    except sqlite3.Error as e:
        print(f"Ошибка при обновлении статуса: {e}")


def get_status(user_id):
    try:
        connection = sqlite3.connect('datapsycho.db')
        sql = connection.cursor()


        sql.execute("SELECT status FROM user_status WHERE user_id = ?", (user_id,))
        result = sql.fetchone()
        current_status = result[0] if result else 0

        return current_status

    except sqlite3.Error as e:
        print(f"Ошибка при получении статуса: {e}")



# sql.execute('CREATE TABLE users(user_id integer, name text, phone_number text, time_sub datetime, end_sub datetime, gender text, status text, amount_sub integer);')
# sql.execute('CREATE TABLE paid(user_id integer, name text, phone_number text, time_sub datetime, end_sub datetime, gender text, status text, amount_sub integer);')
# sql.execute('CREATE TABLE user_status(user_id integer, status integer);')
