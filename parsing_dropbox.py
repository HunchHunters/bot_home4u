import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5Lh-b0BC-970HQOmCnZ1rI1YF1yFqAeJD5sBP1apvbnjx3GfpL-InnxgAGlf1_uWNq7NUUe1dpXoek7Ylr_zFNTpRpPRJzGQe_X6U6CS-qdnhMI-1ol14ogHbLbitEEVz-8AJbcS8Ub')

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
