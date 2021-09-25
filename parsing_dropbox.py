import dropbox
import re
import requests



def photo(url_gsheet):
    try:
        dbx = dropbox.Dropbox('sl.A5Li1Tc-Dcp-vFiw6W-2rKXNkNXjh7uiW-suIrtDzli8VnQLkUfbkxbQu0ktC7QNoK7A8795xp1iInIRrO8hpG6fmaZ-TTw3yUWchPuhqtwcVN5od5ABculB9DBCe42X3895HwI8o09N')

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
