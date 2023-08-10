from IPython.display import clear_output


def markup_activities_type(activity_types):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"

            get_activities = '''SELECT * FROM activities WHERE activity_type is NULL'''

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(get_activities)
                for el in cursor:
                    activity_id = el[0]
                    activity_name = el[2]
                    print(
                        '==============================================================================')
                    print(f'ACTIVITY NAME: {activity_name}')
                    #print('What type of activity this is?')
                    print('\n'.join([str(i) + ' - ' + activity_types[i - 1]
                                     for i in range(1, len(activity_types) + 1)]))
                    type_num = input('SELECT ACTIVITY TYPE:')

                    try:
                        activity_type = activity_types[int(type_num) - 1]
                        update_activity(
                            activity_id, {'activity_type': activity_type})
                        clear_output(wait=False)
                    except Error as e:
                        print(f'ERROR: {e}')

    except Error as e:
        print(e)


def markup_activities_sentiment(activity_emotions):
    try:
        with connect(host=db_host, user=db_user, password=db_password,) as connection:
            use_db_query = f"USE {db_name};"
            get_activities = '''SELECT * FROM activities WHERE activity_emotion is NULL'''

            with connection.cursor() as cursor:
                cursor.execute(use_db_query)
                cursor.execute(get_activities)
                for el in cursor:
                    activity_id = el[0]
                    activity_name = el[2]
                    print(
                        '==============================================================================')
                    print(f'ACTIVITY NAME: {activity_name}')
                    #print('What type of activity this is?')
                    print('\n'.join([str(i) + ' - ' + activity_emotions[i - 1]
                                     for i in range(1, len(activity_emotions) + 1)]))
                    emotion_num = input('SELECT ACTIVITY SENTIMENT:')

                    try:
                        activity_emotion = activity_emotions[int(
                            emotion_num) - 1]
                        update_activity(
                            activity_id, {'activity_emotion': activity_emotion})
                        clear_output(wait=False)
                    except Error as e:
                        print(f'ERROR: {e}')

    except Error as e:
        print(e)
