import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5JKyROSHCtRx7Bc_t1UYxbBDLOxlBUHL9cYVGPh09_ZEvcUw0btliKm8f64yAk46m7NKTYPmxn9HowAw4HLrddPvGF1k3vOvtthpAK6-WNsDiVwmqCPVTNouSJO9TL4775lcVT_ZFLQ')

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
