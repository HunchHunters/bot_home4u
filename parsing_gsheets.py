import gspread


def getListFromUsername(username):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Tilda_Form_4559105_20210916132823").sheet1
    cell = sheet.find(username)
    row = cell.row

    return sheet.row_values(row)
