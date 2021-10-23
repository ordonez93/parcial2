

def getDatabases(DB):
    
    cursor = DB.cursor(dictionary=True)

    cursor.execute('SHOW DATABASES')
    
    return cursor.fetchall()


def crearBase(DB,nombre):
    cursor = DB.cursor(dictionary=True)

    cursor.execute('''
        CREATE DATABASE %s
    ''', (nombre))

    DB.commit()
    cursor.close()