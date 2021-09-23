import dropbox
import re
import requests
dbx = dropbox.Dropbox('sl.A5B_asftja8Ujo1l1kxbxKDnF70a8K1B2glrezKQ8olu8REdTvfbLOdmH8fJ62bVC5Fo-xF5t3xLPX6dpw349AoueOtElFxlAPukVqjM2do9Q6vTtDjN_VweL3Mt5DlXjoc2Lrka8W0_')


def photo(url_gsheet):
    req_bytes = requests.get(url_gsheet).content
    my_json = req_bytes.decode()
    str = my_json
    exp = r'\w{2,}(.png|.jpg)</'
    result = re.search(exp, str).group(0)
    # start_index = my_json.find('?dl=0">')
    # finish_index = my_json.find('</a>')
    file_name = result[1:]
    metadata, f = dbx.files_download('/Приложения/Tilda Publishing/' + '1632338892394_tilda6669157.jpg')
    return f.content
