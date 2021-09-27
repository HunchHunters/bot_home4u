import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5UVVOCM2MPHZKerwKx0_jgxoo4DpTkqt9d39V9X0wILX8sjp6FdI4jRfEQ_6Pit7dHrO2oWkV9bLHA-PvZ_-1IPVQQQBUT0dGiqAPW-iegjJGHR9-brVDi_hfQ15ZQKZEUS94VUot3n')

    except AuthError:
        raise TypeError

    req_bytes = requests.get(url_gsheet).content
    my_json = req_bytes.decode()
    str = my_json
    exp = r'>.{2,}(.png|.jpg|.jpeg)'
    result = re.search(exp, str).group(0)
    result = result[1:]
    # start_index = my_json.find('?dl=0">')
    # finish_index = my_json.find('</a>')
    file_name = result
    metadata, f = dbx.files_download('/Приложения/Tilda Publishing/' + file_name)
    return f.content
