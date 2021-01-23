# TABLE MANAGEMENT ####################################################################################################
def init_db():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    try:
        c.execute(
            '''CREATE TABLE existing_videos (
                id text, upload_date text, existing_playlist_id text, 
                created_playlist_id text, playlist_order text, processed bool)''')
    except sqlite3.OperationalError as err:
        print(err)

    try:
        c.execute('''CREATE TABLE existing_playlists (id text, date text)''')
    except sqlite3.OperationalError as err:
        print(err)

    try:
        c.execute('''CREATE TABLE created_playlists (id text, start_date text, end_date text)''')
    except sqlite3.OperationalError as err:
        print(err)

    conn.commit()
    conn.close()


def drop_database():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS existing_videos''')
    c.execute('''DROP TABLE IF EXISTS existing_playlists''')
    c.execute('''DROP TABLE IF EXISTS created_playlists''')
    conn.commit()
    conn.close()

