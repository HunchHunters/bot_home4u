from oauth2client.service_account import ServiceAccountCredentials
import gspread
# Google
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)

#creds = ServiceAccountCredentials.from_json('mypython-326612-6af17f4344e7.json')

client = gspread.authorize(creds)

python_test = client.open("Tilda_Form_4559105_20210916132823").sheet1
# Указываем путь к JSON


print(python_test.cell(1,1).value)
























# import httplib2
# import apiclient.discovery
# from oauth2client.service_account import ServiceAccountCredentials
# import subprocess
#
#
# CREDENTIALS_FILE = 'mypython-326612-6af17f4344e7.json'  # Имя файла с закрытым ключом, вы должны подставить свое
#
# # Читаем ключи из файла
# credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
#
# httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
# service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API
#
# results = service.spreadsheets().values().batchUpdate(spreadsheetId = '1N9CrANUDzMGQ8I-nQGwcrCXUQRPM78cUHb8KuRKn3Bo', body = {
#     "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
#     "data": [
#         {"range": "Лист номер один!A2:B10",
#          "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
#          "values": [
#                     ["Text message", "File_id"], # Заполняем первую строку
#                     ['result = p.communicate()[0]', 'Id']  # Заполняем вторую строку
#                    ]}
#     ]
# }).execute()
#
# p=subprocess.Popen(['/usr/bin/python3', '/home/roman/PycharmProjects/uznaemfileID/file_id.py', 'stdout=subprocess.PIPE', 'stderr=subprocess.STDOUT'])
# result = p.communicate()[0]
