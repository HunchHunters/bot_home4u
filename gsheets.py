from oauth2client.service_account import ServiceAccountCredentials
import gspread
# Google
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

#creds = ServiceAccountCredentials.from_json_keyfile_name('mypython-326612-6af17f4344e7.json', scope)

creds = ServiceAccountCredentials.from_json({
  "type": "service_account",
  "project_id": "mypython-326612",
  "private_key_id": "6af17f4344e7e96df0e3af492c5a8ffcb412d193",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyCu3IqFWzd0rz\nMjUtj97eV4vsrGsfeffePYmZmLTXumES3nyGuI3/44DN9aedApN6c18S5+XR4Uao\ntS5YPG2X3deyiuzsNEQL7HyNu8xbqo8Pq2TyldYVWRMT6lalxl3TEt0o3xIUEWPG\nNxfbDZvxqlft1zk3sTio9PaJEPelLZmQMvFMpU28cWYPR+ZP3YQBh/Ei2AKRH/XI\nEzOfW+JLri0HItXPwNAsec9F2UimqDPYbsa4TPIhMkN0H0YLLVp/WXuKejfrJBMe\n+VBJIZV0OmzbEtnB+6ctW4AzM9H0gaXMWuE5yJ+ZbPOgpR/F6pf/AcaOO9xAuKUP\nFLpGRSmdAgMBAAECggEAFdCc/f8SMSEmv9GhDmoYZqnXbTJbFco+Aq8LkxRQ5DXj\n+wnjvCYU0AuyFopI9UYBh/lm5swfLq4pmDZK7WjKDNeTvD6ldPOaetOJF1yxV3H4\ngXUAs3CEgK0fV0tZPoqlqF0hWAatEmRnEzxg4egy+VNj3rKGQjqmtJz/MCAyF7zg\nLzmUTIX0KPYc4AWkqYWr6UICIo1+mmgAt1LnxnPSHckL15AKQ88hY23tLvM2ANND\n55/l3V4HxeNpEDYQzbWON109GEW+xJ7RzfMH3c0WRC+7eh/t3SWYMfN7F2Tctwi5\nNzjK1rryXH0ffdTwvIv314U/erzF2Jsw9dBWVUgLSQKBgQDjEHyRQWCnNABav+ZU\n/pft/2Fl+R3YIU6ZJPuGxbzD5VROVxoaFRobUgsHFcgtOxQ2W3Rpk9uLSsd62aGJ\nwHTKkol//OAb9udzDMfF5HlTRUEshiNq2Hmi3Tc2Iw9Ovost2etUPrGS1sN0LVnP\njObEJRXdECK+NEsxsD1AR3UkdwKBgQDIuzV3P+02aYJDzEWurJEY0O4BzdwMujUc\npIHdpcv9AGyQTlsugOcxvjVgrQaOYUWrJP6GSqOb46RD/i1dS5omkA7FwShj7a6+\nZZDuykMBCwM1buenoAJC0C8Ybd9kaub3eHX9FnNG7adEUEaTsrZIKtz1zIQW7VfJ\nKR0ZSEDLiwKBgBKAWWYMia+WESFT2ZS7We3OjUUd00y1Cg54cPY+Tm831HK9ribJ\n6WKogLWHFNR6p971/LpNjen/odlkukDbKakH36RKGoisyZcaR3zcbPZYAkN6epBO\nKzsWA1Wp7alg5T5LL12h7h4k2bAxscuzk2oQC4QDuJD++dGGprcCG41pAoGBALuR\n9EwSeF84CHnCD/tBVfSSh1U4QD/EYIz7TD8KBqvMEaZnEd1Kpr9cthQ4mr/BNZDP\naOekJ24sMfs3MLzVQJ54TtWLwWpfV8KitePtLN90ovLzR5TjeDlmwBtb0DvNiTYG\nYnq019OXj43OVaT+gka9huxIx8WE01suB/rwAVwxAoGATen5hRN13wgMv6PXEkN+\ncYLtUvxu/gcMQrnbaG3RFiSybgdoVEPOjmpAZrp69nOa7ooAQoajtUtrFDIBm5SV\nF+lBE8VXcwq/vSNyIKCIR9mjn2vg/kkbBLfZimA/rQnqd9+tzkHENpHAO4JBEzhM\nLg4etuQCUbzzLs6hVUqlD7o=\n-----END PRIVATE KEY-----\n",
  "client_email": "acc-736@mypython-326612.iam.gserviceaccount.com",
  "client_id": "115290582684655512854",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/acc-736%40mypython-326612.iam.gserviceaccount.com"
}
)

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
