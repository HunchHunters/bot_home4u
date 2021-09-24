list_users = ['followthesun', 'Ad_dregal']

def obtain_songs(list_users):
    import sqlite3
    import random
    connection = sqlite3.connect('db_spotify.db')
    cursor = connection.cursor()
    users_rand_songs = []
    for username in list_users:
        cursor.execute("SELECT * FROM SpotifyMatching WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        connection.commit()
        playlist_user = user_data[1].split('/next/')
        playlist_user = playlist_user[1:]
        users_rand_songs.append(random.sample(playlist_user,5))
    print(users_rand_songs)

obtain_songs(list_users)

def parsing(username):
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
    sorted_keys = sorted(scores_dict, key=scores_dict.get, reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]
    del sorted_dict['followthesun']
    list_to_match = list(sorted_dict.keys())
    song_matches = []
    return list_to_match

class ListIterator:
    def __init__(self, list_iter):
        self.list = list_iter
        self.limit = len(list_iter)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            index = self.counter
            self.counter += 1
            return self.list[index]
        else:
            raise StopIteration
