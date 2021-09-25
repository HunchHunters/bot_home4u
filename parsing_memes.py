
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def find_name(username):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
    client = gspread.authorize(creds)
    spreadsheet  = client.open("Tilda_Form_4559105_20210922195121")
    sheet = spreadsheet.sheet1
    if (end_time - start_time).total_seconds() < 1:
        sleep(1.01 - (end_time - start_time).total_seconds())

    cell = sheet.find(username)
    row = cell.row
    name = sheet.row_values(row)[0]
    return name

def find_link_photo(username):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
    client = gspread.authorize(creds)
    spreadsheet  = client.open("Tilda_Form_4559105_20210922195121")
    sheet = spreadsheet.sheet1
    if (end_time - start_time).total_seconds() < 1:
        sleep(1.01 - (end_time - start_time).total_seconds())

    cell = sheet.find(username)
    row = cell.row
    link = sheet.row_values(row)[27]
    print(link)
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

def meme_matching( username):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
    client = gspread.authorize(creds)
    spreadsheet  = client.open("Tilda_Form_4559105_20210922195121")
    sheet = spreadsheet.sheet1
    list_of_dicts = sheet.get_all_records()
    len_list = len(list_of_dicts)
    users = sheet.col_values(2)[1:]
    amount_of_users = len(users)
    scores_list = [i for i in range(amount_of_users)]
    scores_dict = dict(zip(users, scores_list))
    cell = sheet.find(username)
    row = cell.row
    print(row)
    memes_1 = sheet.col_values(23)[1:]
    ###################
    for meme, user in zip(memes_1, users):
        if meme == memes_1[row-2]:
            scores_dict[user] =int(scores_dict[user]) + 1
    memes_2 = sheet.col_values(24)[1:]
    #####################
    for meme, user in zip(memes_2, users):
        if meme == memes_2[row-2]:
            scores_dict[user] =int(scores_dict[user]) + 1
    ####################
    memes_3 = sheet.col_values(25)[1:]
    for meme, user in zip(memes_3, users):
        if meme == memes_3[row-2]:
            scores_dict[user] =int(scores_dict[user]) + 1
    ########################
    memes_4 = sheet.col_values(26)[1:]
    for meme, user in zip(memes_4, users):
        if meme == memes_4[row-2]:
            scores_dict[user] =int(scores_dict[user]) + 1
    ###################
    memes_5 = sheet.col_values(27)[1:]
    for meme, user in zip(memes_5, users):
        if meme == memes_5[row-2]:
            scores_dict[user] = int(scores_dict[user]) + 1

    sorted_dict = {}
    sorted_keys = sorted(scores_dict, key=scores_dict.get,reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]

    list_to_match = list(sorted_dict.keys())[1:]

    UsernamesNamesPhotos = {}

    for name in list_to_match:
        cell = sheet.find(name)
        row = cell.row
        UsernamesNamesPhotos[name] = [sheet.row_values(row)[0], sheet.row_values(row)[27]]

    return UsernamesNamesPhotos
