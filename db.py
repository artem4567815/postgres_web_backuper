import psycopg2

def get_first_data(conn_params):
    result = []
    try:
        # Создаем подключение к базе данных
        conn = psycopg2.connect(**conn_params)

        # Создаем курсор для выполнения SQL-запросов
        cursor = conn.cursor()

        # Получаем список всех баз данных
        cursor.execute("SELECT datname FROM pg_database")
        databases = cursor.fetchall()

        # Закрываем курсор и соединение с базой данных
        cursor.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с базой данных:", error)

    for i in databases:
        res_dict = {}
        conn_params["database"]=i[0]
        try:
            # Создаем подключение к базе данных
            conn = psycopg2.connect(**conn_params)
            res_dict["name"] = i[0]

            # Создаем курсор для выполнения SQL-запросов
            cursor = conn.cursor()

            # Получаем список всех схем в базе данных
            cursor.execute("SELECT schema_name FROM information_schema.schemata")
            schemas = cursor.fetchall()

            fdf = []
            for schema in schemas:
                fdf.append(schema[0])
            res_dict["schemas"] = fdf

            # Закрываем курсор и соединение с базой данных
            cursor.close()
            conn.close()
            result.append(res_dict)

        except (Exception, psycopg2.Error) as error:
            print("Ошибка при работе с базой данных:", error)
    return result
