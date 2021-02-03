import sqlite3
from discord_database import DATABASE_NAME


def write_buy_price(user_id, price, date):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    row = get_buy_row(user_id, date)
    if row is None:
        print(f'Inserting {price} for {date},{user_id}')
        c.execute('''INSERT INTO ac_turnip_buy (id,date,price) VALUES (:user_id, :date, :price)''',
                  {'user_id': user_id, 'date': date, 'price': price})
    else:
        print(f'Updating {price} for {date},{user_id}')
        c.execute('''UPDATE ac_turnip_buy SET price = :price WHERE id = :user_id AND date = :date''',
                  {'user_id': user_id, 'date': date, 'price': price})
    conn.commit()
    conn.close()


def write_sell_price(user_id, price, date):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    row = get_sell_row(user_id, date)
    if row is None:
        print(f'Inserting {price} for {date},{user_id}')
        c.execute('''INSERT INTO ac_turnip_sell (id,date,price) VALUES (:user_id, :date, :price)''',
                  {'user_id': user_id, 'date': date, 'price': price})
    else:
        print(f'Updating {price} for {date},{user_id}')
        c.execute('''UPDATE ac_turnip_sell SET price = :price WHERE id = :user_id AND date = :date''',
                  {'user_id': user_id, 'date': date, 'price': price})
    conn.commit()
    conn.close()


def get_buy_row(user_id, date):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(
        '''SELECT id,price,date
        FROM ac_turnip_buy WHERE id = :user_id AND date = :date''',
        {'user_id': user_id, 'date': date})
    row = c.fetchone()
    conn.close()
    return row


def get_sell_row(user_id, date):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(
        '''SELECT id,price,date
        FROM ac_turnip_sell WHERE id = :user_id AND date = :date''',
        {'user_id': user_id, 'date': date})
    row = c.fetchone()
    conn.close()
    return row
