import datetime
import sqlite3

DATABASE_NAME = 'discord.db'


def main():
    while True:
        print('[0] Delete database')
        print('[1] Create database')
        print('[2] Backup database')
        input_value = input('Option: ')

        if input_value == '1':
            init_db()
            print('Database created')
        elif input_value == '2':
            backup()
            print('Database backed up')
        elif input_value == '0':
            confirm = input('Delete database y/n: ')
            if confirm == 'y':
                drop_database()
                print('Database deleted')
        else:
            break
        print('')

    print('Done.')


# TABLE MANAGEMENT ####################################################################################################
def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # User info across games such as Nintendo friend codes
    try:
        c.execute(
            '''CREATE TABLE user_info (
                id text, nickname text, friend_code text)''')
    except sqlite3.OperationalError as err:
        print(err)

    # Table that tracks number of times the Phasmophobia Betty Bot has been taunted
    try:
        c.execute('''CREATE TABLE betty_bot (id text, rage number)''')
    except sqlite3.OperationalError as err:
        print(err)

    # User info for Animal Crossing such as town name and fruits
    try:
        c.execute('''CREATE TABLE ac_info (id text, town_name text, fruit text)''')
    except sqlite3.OperationalError as err:
        print(err)

    # Turnip prices
    try:
        c.execute('''CREATE TABLE ac_turnip_buy (id text, price number, date text)''')
    except sqlite3.OperationalError as err:
        print(err)

    # Turnip prices
    try:
        c.execute('''CREATE TABLE ac_turnip_sell (id text, price number, date text)''')
    except sqlite3.OperationalError as err:
        print(err)

    conn.commit()
    conn.close()


def backup():
    date = datetime.datetime.now().strftime("%Y%m%d")

    con = sqlite3.connect(DATABASE_NAME)
    bck = sqlite3.connect(date + '-' + DATABASE_NAME)
    with bck:
        con.backup(bck)
    bck.close()
    con.close()


def drop_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS user_info''')
    c.execute('''DROP TABLE IF EXISTS betty_bot''')
    c.execute('''DROP TABLE IF EXISTS ac_info''')
    c.execute('''DROP TABLE IF EXISTS ac_turnip_buy''')
    c.execute('''DROP TABLE IF EXISTS ac_turnip_sell''')
    conn.commit()
    conn.close()


main()
