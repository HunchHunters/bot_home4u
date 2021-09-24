import gspread
from oauth2client.service_account import ServiceAccountCredentials


def find_name(sheet, username):

    cell = sheet.find(username)
    row = cell.row
    name = sheet.row_values(row)[0]
    return name

def find_link_photo(sheet, username):

    cell = sheet.find(username)
    row = cell.row
    link = sheet.row_values(row)[27]
    print(link)
    return link

def find_name(sheet, username):

    cell = sheet.find(username)
    row = cell.row
    link = sheet.row_values(row)[0]
    return link

def meme_matching(sheet, username):

    list_of_dicts = sheet.get_all_records()
    len_list = len(list_of_dicts)
    users = sheet.col_values(2)[1:]
    amount_of_users = len(users)
    scores_list = [i for i in range(amount_of_users)]
    scores_dict = dict(zip(users, scores_list))
    cell = sheet.find(username)
    row = cell.row
    memes_user = sheet.row_values(row)[2:4]
    memes_1 = sheet.col_values(3)[1:]

    for meme, user in zip(memes_1, users):
        if meme == memes_1[0]:
            scores_dict[user] =int(scores_dict[user]) + 1

    sorted_dict = {}
    sorted_keys = sorted(scores_dict, key=scores_dict.get,reverse = True)  # [1, 3, 2]
    for _ in sorted_keys:
        sorted_dict[_] = scores_dict[_]
    list_to_match = list(sorted_dict.keys())[1:]
    return list_to_match
