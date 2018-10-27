import pymysql.cursors
# Connect to the database
def simpleCon():
    
    connection = pymysql.connect(host='35.225.130.71',
                                user='root',
                                password='ShushTush2018',
                                db='STDB',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('kaki@khar2a.com', 'ver2y-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users`"# WHERE `email`=%s"
            cursor.execute(sql)#, ('webmaster@python.org',))
            result = cursor.fetchall()
            row = [item['id'] for item in result]
            #for item in result:
            print(result)
    finally:
        connection.close()

def test1():
    connection = pymysql.connect(host='35.225.130.71',
                                user='root',
                                password='ShushTush2018',
                                db='ANNA',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `PDES`, `UNIT` FROM `PARTS`"# WHERE `PDES`=%s"
            cursor.execute(sql)#, ('מפיות',))
            result = cursor.fetchall()
            print(result)

test1()
        