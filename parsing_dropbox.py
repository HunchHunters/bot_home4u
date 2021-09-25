import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5KHwD4NCJswC_EbPwv6xkxs1Koq3bFabhfVlq31iVt_1TppsX9IMHpb42HpxZh--X98cvel1_9ifXi9UGy4aXWoQS_00AYdkwj1e4B3RoB_7ahY2kYvzIjKwnFFoljnYYdwEWTjcdv7')

    except AuthError:
        raise TypeError

    req_bytes = requests.get(url_gsheet).content
    my_json = req_bytes.decode()
    str = my_json
    print(str)
    exp = r'>.{2,}(.png|.jpg|.jpeg)'
    result = re.search(exp, str).group(0)
    result = result[1:]
    # start_index = my_json.find('?dl=0">')
    # finish_index = my_json.find('</a>')
    file_name = result
    metadata, f = dbx.files_download('/Приложения/Tilda Publishing/' + file_name)
    return f.content
