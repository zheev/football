import psycopg2

# инициализируем бд
def init_db():
    conn = psycopg2.connect(dbname='football', user='football',
                            password='football', host='psql')
    return conn


def clear_url(url):
    url = url.strip('/')
    url = url.replace('/', '_')
    url = url.replace('-', '_')
    url = "\"" + url + "\""
    return url


# добавляем урл в таблицу
def add_url(url):
    conn = init_db()
    cursor = conn.cursor()
    queryText = """
            insert into walls  
            (url)
            values
            (%s) on conflict (url) do nothing
        """
    cursor.execute(queryText.strip(), [url])
    conn.commit()
    conn.close()


def check_url(url):
    conn = init_db()
    cursor = conn.cursor()
    queryText = """
               select url
               from walls
               where url=%(url)s
           """
    cursor.execute(queryText.strip(), {"url":url})
    if len(cursor.fetchall()) > 0:
        conn.close()
        return True
    else:
        conn.close()
        return False


def add_text(text, header, url):
    conn = init_db()
    cursor = conn.cursor()
    queryText = """
                   insert into texts  
                    (text, header, url)
                    values
                    (%(text)s, %(header)s, %(url)s) RETURNING id
               """
    cursor.execute(queryText, {"text":text, "header":header, "url":url})
    conn.commit()
    last_id = cursor.fetchone()[0]
    conn.close()
    return last_id


def get_text(id):
    conn = init_db()
    cursor = conn.cursor()
    queryText = """
       select text, header from texts where id=%s
       """
    cursor.execute(queryText, [id])
    return cursor.fetchone()


