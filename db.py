import sqlite3

name_db = './football.db'

#инициализируем бд
def init_db():
    conn = sqlite3.connect(name_db)
    create_table(conn)
    return conn

# если нет нужной таблицы, то создаём
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
            create table if not exists walls 
            (
                id int primary key,
                url text not null
            )
        """
    )


# добавляем урл в таблицу
def add_url(url):
    conn = init_db()
    cursor = conn.cursor()
    cursor.executemany(
        """
            insert into walls  
            (url)
            values
            (?)
        """, url
    )
    conn.commit()


def get_last_url():
    pass

def check_url():
    pass