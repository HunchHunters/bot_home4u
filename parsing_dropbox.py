import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5J_Hdgm-fUIBWurJouOcGuL2ZKrxLYn0vyu2O1W01cLryq94DP1XBPsp7xa1H4BYWU3zRsps_CauZEF4kJZixl0dCK8s-FYnaCQ-1y4nsoCXCh7viB2FKjomNpsx9D8ZadRbONv9MKs')

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
