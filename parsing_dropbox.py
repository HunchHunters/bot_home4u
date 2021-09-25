import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5IqOAZoLsWhYPiyX4vEERcl8SYwB4qKP1rXBTu4WHmALnqplm2fGlEsxh-1sWS7FzwxU_ma2UF24CEzUGsjc_vUIeSUzszrbQfxIrURJBfHOdhjB9ZVhUHSfVtfGC4glqlokeuqG8lN')

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
