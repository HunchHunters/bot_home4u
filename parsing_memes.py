import gspread
from oauth2client.service_account import ServiceAccountCredentials
from spotipy.oauth2 import SpotifyOAuth
import time

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
client = gspread.authorize(creds)
spreadsheet  = client.open("_Tilda_Form_4559105_20210922195121X_")
sheet = spreadsheet.sheet1


def find_link_photo(username, sheet):
    time.sleep(1.5)
    cell = sheet.find(username)
    row = cell.row
    link = sheet.row_values(row)[27]
    return link

# def find_name(username):
#     import gspread
#     from oauth2client.service_account import ServiceAccountCredentials
#     start_time = datetime.datetime.now()
#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#     creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
#     client = gspread.authorize(creds)
#     sheet = client.open("Tilda_Form_4559105_20210922195121").sheet1
#     end_time = datetime.datetime.now()
#     if (end_time - start_time).total_seconds() < 1:
#         sleep(1.01 - (end_time - start_time).total_seconds())
#
#     cell = sheet.find(username)
#     row = cell.row
#     link = sheet.row_values(row)[0]
#     return link

def meme_matching(username, sheet):
    time.sleep(1)
    if username[0] == '@':
        username = username[1:]
    list_of_dicts = sheet.get_all_records()
    len_list = len(list_of_dicts)
    time.sleep(1)
    users_dict = {}
    scores_dict = {}
    for data in list_of_dicts:
        if data['telegram'][0] == '@':
            data['telegram'] = data['telegram'][1:]
        users_dict[data['telegram']] = [data['name'],
                                data['Фото_которым_вы_хотите_поделиться_ваша_фотография_любимый_мем_и_т_д_'],
                                data['meme_form1'],
                                data['meme_form2'],
                                data['meme_form3'],
                                data['meme_form4'],
                                data['meme_form5']]
        scores_dict[data['telegram']] = 0


    memes_1, memes_2, memes_3, memes_4, memes_5 = [],[],[],[],[]

    users_list = list(users_dict.keys())

    for user in users_list:
        if users_dict[user][2] == users_dict[username][2]:
            scores_dict[user] = scores_dict[user] + 1
        if users_dict[user][3] == users_dict[username][3]:
            scores_dict[user] = scores_dict[user] + 1
        if users_dict[user][4] == users_dict[username][4]:
            scores_dict[user] = scores_dict[user] + 1
        if users_dict[user][5] == users_dict[username][5]:
            scores_dict[user] = scores_dict[user] + 1
        if users_dict[user][6] == users_dict[username][6]:
            scores_dict[user] = scores_dict[user] + 1

    sorted_dict = {}
    sorted_keys = sorted(scores_dict, key=scores_dict.get, reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]

    list_to_match = list(sorted_dict.keys())[1:]
    print(list_to_match)

    dict_to_match = {}
    for user in list_to_match:
        dict_to_match[user] = [users_dict[user][0], users_dict[user][1]]

    return dict_to_match
