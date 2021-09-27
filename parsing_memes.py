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

def getDictFromUsername(username):
    print(username)
    time.sleep(1)
    cell = sheet.find(username)
    rowNum = cell.row
    time.sleep(1)
    row = sheet.row_values(rowNum)
    time.sleep(1)
    headRow = sheet.row_values(1)

    return dict(zip(headRow, row))

def strValuesToNum(dictionary):
    for key in dictionary.keys():
        try:
            dictionary[key] = int(dictionary[key])
        except ValueError:
            continue

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
                                data['meme_form5'],
                                data['budget'],
                                data['bedtime']
                                ]
        scores_dict[data['telegram']] = 0


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

    d_scores = {}
    for user in scores_dict:
        norming_meme_score = scores_dict[user]/6
        compatibility = habbitsTest(username, user)
        scores_dict[user] = compatibility * norming_meme_score

    sorted_dict = {}
    sorted_keys = sorted(scores_dict, key=scores_dict.get, reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]

    list_to_match = list(sorted_dict.keys())[1:]

    dict_to_match = {}
    for user in list_to_match:
        dict_to_match[user] = [users_dict[user][0], users_dict[user][1],users_dict[user][7], users_dict[user][8], scores_dict[user][0], d_scores[user][1]]

    print(dict_to_match)
    return dict_to_match


def unifyString(string):
    return string.replace(' ', '').replace('-', '').lower()

def banCheck(ans1, ans2):
    # Gender check.
    same_sex_important = \
        ans1['sex_importance'] == 'Важно' or \
        ans2['sex_importance'] == 'Важно'
    different_sex = ans1['sex'] != ans2['sex']
    if same_sex_important and different_sex:
        print('Ban for gender')
        return False

    # COVID check.
    if ans1['vaccination_importance'] == 'Да' and \
       ans2['vaccination_status'] == 'Не вакцинирован' or \
       ans2['vaccination_importance'] == 'Да' and \
       ans1['vaccination_status'] == 'Не вакцинирован':
        print('Ban for COVID')
        return False

    # # Metro station check.
    # metro1 = set(unifyString(ans1['metro']).split(','))
    # metro2 = set(unifyString(ans2['metro']).split(','))
    # common_stations = metro1 & metro2
    # if len(common_stations) < 1:
    #     print('Ban for metro')
    #     return False
    # print(f'Common metro stations: {common_stations}')

    # Smoke check.
    if ans1['smoke_tolerance'] == 'Да' and ans2['smokes'] == 'Да' or \
       ans2['smoke_tolerance'] == 'Да' and ans1['smokes'] == 'Да':
        print('Ban for smoking')
        return False

    return True

def habbitsCompatibility(ans1, ans2):

    # First make it 100, then penalize them for different habbits.
    compatibility = 100.

    if not banCheck(ans1, ans2):
        compatibility = 0.
        return compatibility

    # Each of the following checks substracts
    # from 0 to 10 compatibility points.
    # 10 checks in total.

    # <----------------------------------------------------------------------->
    # 1) Age check.
    ageToNum = {
        '18-22': 1,
        '23-25': 2,
        '26-28': 3,
        '28-30': 4,
        'Более 30': 5
    }
    dist = abs(ageToNum[ans1['age']] - ageToNum[ans2['age']])  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for age')

    # <----------------------------------------------------------------------->
    # 2) Budget check.
    budgetToNum = {
        '15-20 тыс. руб.': 1,
        '20-25 тыс. руб.': 2,
        '25-30 тыс. руб.': 3,
        '30-35 тыс. руб.': 4,
        'Более 35 тыс. руб.': 5
    }
    dist = abs(
        budgetToNum[ans1['budget']] -
        budgetToNum[ans2['budget']]
    )  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for budget')

    # <----------------------------------------------------------------------->
    # 3) Guests check.

    # 1-5 -> 0-10
    penalty1 = (ans1['guests_frequency'] - 1) * 2.5
    penalty2 = (ans2['guests_frequency'] - 1) * 2.5

    # [1 2 3 4 5] -> [1 .75 .5 .25 0]
    weight1 = 1.25 - .25 * ans2['guests_attitude']
    weight2 = 1.25 - .25 * ans1['guests_attitude']

    penalty1 *= weight1
    penalty2 *= weight2
    penalty = max(penalty1, penalty2)
    compatibility -= penalty
    print(f'-{penalty} penalty for guests')

    # <----------------------------------------------------------------------->
    # 4) Bedtime check.
    bedtimeToNum = {
        'До 22:00': 1,
        '22:00 - 23:00': 2,
        '23:00 - 00:00': 3,
        '00:00 - 01:00': 4,
        'После 01:00': 5
    }
    dist = abs(
        bedtimeToNum[ans1['bedtime']] -
        bedtimeToNum[ans2['bedtime']]
    )  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for bedtime')

    # <----------------------------------------------------------------------->
    # 5) Noise check.
    weight1 = int(ans1['headphones'] == 'Нет')
    weight2 = int(ans2['headphones'] == 'Нет')

    # 1-5 -> 0-10
    penalty1 = (ans2['noise_tolerance'] - 1) * 2.5
    penalty2 = (ans1['noise_tolerance'] - 1) * 2.5

    penalty1 *= weight1
    penalty2 *= weight2
    penalty = max(penalty1, penalty2)
    compatibility -= penalty
    print(f'-{penalty} penalty for noise')

    # <----------------------------------------------------------------------->
    # 6) Cleaning check.
    frequencyToNum = {
        'Более 1 раза в неделю': 5,
        '1 раз в неделю': 4,
        '1 раз в 2 недели': 3,
        '1 раз в 3 недели': 2,
        'реже': 1
    }
    dist = abs(
        frequencyToNum[ans1['cleaning_frequency']] -
        frequencyToNum[ans2['cleaning_frequency']]
    )  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for cleaning')

    # <----------------------------------------------------------------------->
    # 7) Pets check.
    if ans1['pet_tolerance'] == 1 and ans2['pet'] == 'Да' or \
       ans2['pet_tolerance'] == 1 and ans1['pet'] == 'Да':  # ban
        print('Ban for pets\n')
        return 0

    weight1 = int(ans1['pet'] == 'Да')
    weight2 = int(ans2['pet'] == 'Да')

    # [2 3 4 5] -> [10 20/3 10/3 0]
    penalty1 = -10 / 3 * ans2['pet_tolerance'] + 50 / 3
    penalty2 = -10 / 3 * ans1['pet_tolerance'] + 50 / 3

    penalty1 *= weight1
    penalty2 *= weight2
    penalty = max(penalty1, penalty2)
    compatibility -= penalty
    print(f'-{penalty} penalty for pets')

    # <----------------------------------------------------------------------->
    # 8) Dishes check.
    weight = int(ans1['common_dishes'] != ans2['common_dishes'])
    penalty = weight * 10.
    compatibility -= penalty
    print(f'-{penalty} penalty for dishes')

    # <----------------------------------------------------------------------->
    # 9) Communication check.
    dist = abs(
        ans1['communication_importance'] -
        ans2['communication_importance']
    )  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for communication')

    # <----------------------------------------------------------------------->
    # 10) Common interests check.
    dist = abs(
        ans1['common_interests_importance'] -
        ans2['common_interests_importance']
    )  # 0-4
    penalty = dist * 2.5  # 0-10
    compatibility -= penalty
    print(f'-{penalty} penalty for common interests')

    assert 0 <= compatibility <= 100
    return round(compatibility, 1)

def habbitsTest(username1, username2):

    ans1 = getDictFromUsername(username1)
    ans2 = getDictFromUsername(username2)
    strValuesToNum(ans1)
    strValuesToNum(ans2)
    return habbitsCompatibility(ans1, ans2)

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from parsing_memes import meme_matching, find_link_photo
#
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
# client = gspread.authorize(creds)
# spreadsheet  = client.open("_Tilda_Form_4559105_20210922195121X_")
# sheet = spreadsheet.sheet1
#
# meme_matching('followthesun', sheet)
