config = configparser.ConfigParser()
config.read("config.ini")


db_name = config['database']['db_name']
db_user = config['database']['db_user']
db_password = config['database']['db_password']
db_host = config['database']['db_host']


def update_post(post_id, update_data):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"

            update_post_table_query = ''
            update_values = []

            for key, value in update_data.items():
                update_post_table_query += key + ' = %s, '
                update_values += [value]

            update_post_table_query = update_post_table_query.rstrip(', ')
            update_post_table_query = 'UPDATE posts SET ' + \
                update_post_table_query + ' WHERE post_id = %s;'

            update_values += [post_id]
            update_values = tuple(update_values)

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(update_post_table_query, update_values)
                connection.commit()

            print(f'UPDATED: post with id:{post_id}')
    except Error as e:
        print(e)


def update_activity(activity_id, update_data):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"

            update_activity_table_query = ''
            update_values = []

            for key, value in update_data.items():
                update_activity_table_query += key + ' = %s, '
                update_values += [value]

            update_activity_table_query = update_activity_table_query.rstrip(
                ', ')
            update_activity_table_query = 'UPDATE activities SET ' + \
                update_activity_table_query + ' WHERE activity_id = %s;'

            update_values += [activity_id]
            update_values = tuple(update_values)

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(update_activity_table_query, update_values)
                connection.commit()

            print(f'UPDATED: activity with id:{activity_id}')
    except Error as e:
        print(e)


import mysql.connector

from getpass import getpass
from mysql.connector import connect, Error


def db_connect():
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            create_posts_table_query = """
            CREATE TABLE IF NOT EXISTS posts(
                post_id INT,
                text TEXT,
                parsed_date DATE,
                upload_date DATETIME,
                edit_date DATETIME, 
                productivity_score FLOAT,
                interest_score FLOAT,
                stress_score FLOAT,
                predicted_productivity_score FLOAT,
                predicted_interest_score FLOAT,
                predicted_stress_score FLOAT,
                PRIMARY KEY (post_id)
            );
            """

            create_posts_table_activities = """
            CREATE TABLE IF NOT EXISTS activities(
                activity_id INT AUTO_INCREMENT,
                post_id INT,
                activity_name TEXT,
                activity_emoji TEXT,
                activity_type TEXT,
                activity_emotion TEXT,
                predicted_activity_type TEXT,
                predicted_activity_emotion TEXT,
                FOREIGN KEY (post_id) REFERENCES posts(post_id),
                PRIMARY KEY (activity_id)
            );
            """

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(create_posts_table_query)
                cursor.execute(create_posts_table_activities)
                connection.commit()
    except Error as e:
        print(e)


def upload_post(dct, overwrite=False):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            check_if_exist = """SELECT EXISTS(SELECT 1 FROM posts WHERE post_id = %s LIMIT 1)"""

            upload_posts_table_query = f"""
            INSERT INTO posts (post_id, text, parsed_date, upload_date, 
            edit_date,productivity_score, interest_score, stress_score, 
            predicted_productivity_score, predicted_interest_score,
            predicted_stress_score) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            post_id = (dct.get('post_id', None),)
            uploaded_date = dct.get('upload_date', None)

            insert_data = (dct.get('post_id', None), dct.get('text', None),
                           dct.get('parsed_date', None), dct.get(
                               'upload_date', None),
                           dct.get('edit_date', None), dct.get(
                               'productivity_score', None),
                           dct.get('interest_score', None), dct.get(
                               'stress_score', None),
                           dct.get('predicted_productivity_score', None), dct.get(
                               'predicted_interest_score', None),
                           dct.get('predicted_stress_score', None))

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(check_if_exist, post_id)
                for el in cursor:
                    exist = el[0]

                if not exist:
                    cursor.execute(upload_posts_table_query, insert_data)
                    connection.commit()
                    print(
                        f'UPLOADED: post with id:{post_id} and uploaded_date:{uploaded_date}')
                else:
                    if overwrite:
                        pass
                        print(
                            'OVERWRITED: post with id:{post_id} and uploaded_date:{uploaded_date}')
                    else:
                        print(
                            f'ERROR: post with id:{post_id} and uploaded_date:{uploaded_date} already uploaded')
                        print('If you want to overwrite data add flag')
    except Error as e:
        print(e)


def upload_activities(dct, overwrite=False):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"

            for activity_emoji, activity_name in dct['parsed_activities']:

                # add or not?
                # if activity_emoji == '*' or activity_emoji == '📦':
                #   continue

                activity_name = "".join(c for c in activity_name if c.isalpha(
                ) or c.isnumeric() or c == ' ' or c == '!').strip(' ')
                check_if_exist = """SELECT EXISTS(SELECT 1 FROM activities WHERE post_id = %s AND activity_name = %s LIMIT 1)"""

                upload_posts_table_query = f"""
                INSERT INTO activities (post_id, activity_name, activity_emoji, activity_type, 
                activity_emotion, predicted_activity_type, predicted_activity_emotion) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)
                """
                post_id = dct.get('post_id', None)

                check_data = (post_id, activity_name)

                insert_data = (dct.get('post_id', None), activity_name,
                               activity_emoji, dct.get('activity_type', None), dct.get(
                                   'activity_emotion', None),
                               dct.get('predicted_activity_type', None), dct.get('predicted_activity_emotion', None))

                with connection.cursor() as cursor:
                    cursor.execute(use_db_query)
                    cursor.execute(check_if_exist, check_data)
                    for el in cursor:
                        exist = el[0]

                    if not exist:
                        cursor.execute(upload_posts_table_query, insert_data)
                        connection.commit()
                        print(
                            f'UPLOADED: activity with post_id:{post_id} and activity_name:{activity_name}')
                    else:
                        # add overwrite option
                        print(
                            f'ERROR: activity with post_id:{post_id} and activity_name:{activity_name} already uploaded')
    except Error as e:
        print(e)


def update_post(dct):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            update_posts_table_query = """
            UPDATE posts SET text = %s, parsed_date = %s,  
            upload_date = %s, edit_date = %s, productivity_score = %s,
            interest_score = %s, stress_score = %s WHERE post_id = %s
            """

            data = (dct.get('text', None),
                    dct.get('parsed_date', None), dct.get('upload_date', None),
                    dct.get('edit_date', None), dct.get(
                        'productivity_score', None),
                    dct.get('interest_score', None), dct.get(
                        'stress_score', None),
                    dct.get('post_id', None))

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(update_posts_table_query, data)
                connection.commit()
    except Error as e:
        print(e)


def db_show_tables():
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            show_tables = "SHOW TABLES;"
            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(show_tables)
                for el in cursor.fetchall():
                    print(el)
    except Error as e:
        print(e)


def db_execute_query(query, commit=False):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(query)
                if commit:
                    connection.commit()
                for el in cursor:
                    print(el)
    except Error as e:
        print(e)
