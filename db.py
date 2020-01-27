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
                id integer primary key,
                url text not null,
                unique(url, id)
            )
        """
    )
    cursor.execute(
        """ 
        CREATE UNIQUE INDEX IF NOT EXISTS unique_name ON walls(url);
        """
    )

def clear_url(url):
    url = url.strip('/')
    url = url.replace('/', '_')
    url = url.replace('-', '_')
    url = "\""+url+"\""
    return url

# добавляем урл в таблицу
def add_url(url):
    conn = init_db()
    cursor = conn.cursor()
    queryText =  """
            insert or ignore into walls  
            (url)
            values
            ({url})
        """.format(url=clear_url(url))
    cursor.execute(queryText)
    conn.commit()


def check_url(url):
    conn = init_db()
    cursor = conn.cursor()
    queryText = """
               select url
               from walls
               where url={url}
           """.format(url=clear_url(url))
    cursor.execute(queryText)
    if len(cursor.fetchall()) > 0:
        return True
    else:
        return False