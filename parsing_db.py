
def parsing_db(username):
    import sqlite3
    connection = sqlite3.connect('db_spotify.db')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM SpotifyMatching")
    data = cursor.fetchall()
    connection.commit()

    cursor.execute("SELECT * FROM SpotifyMatching WHERE username = ?", (username,))
    user_data = cursor.fetchone()
    connection.commit()

    users = cursor.execute("SELECT username FROM SpotifyMatching")
    users = cursor.fetchall()
    connection.commit()
    users_to_compare = []
    for user in users:
        users_to_compare.append(user[0])

    amount_of_users = len(users_to_compare)
    scores_list = [0 for i in range(amount_of_users)]
    scores_dict = dict(zip(users_to_compare, scores_list))
    print(user_data)
    playlist_user = user_data[1].split(' ')

    for song, user in zip(data, users_to_compare):
        print(song[1])
        print(user_data[1])
        if song[1] in user_data[1]:
            scores_dict[user] = scores_dict[user] + 1

    print(scores_dict)
    sorted_dict = {}
    sorted_keys = sorted(scores_dict, key=scores_dict.get,reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]
    del sorted_dict['followthesun']
    list_to_match = list(sorted_dict.keys())
    return list_to_match
    #
    #
    #
    # user_data_list = user_data[1].split(' ')
    #
    # for elem in data:
    # print(user_data_list)

print(parsing_db('followthesun'))
