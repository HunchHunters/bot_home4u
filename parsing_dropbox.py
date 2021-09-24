import dropbox
import re
import requests
dbx = dropbox.Dropbox('sl.A5Eu7JAHSplw774HXkeV_pRmqNwaVJc2T7rTEFBMwAepfnnfGtj7oXDQXAtl4WeT0awnjOvBCPEl889_RYgySUZlqJSxBjCORqTTVJlR4Q67qaPKTK3_NB-M7socXUmqTIUPohP8TNl4')

def photo(url_gsheet):
    req_bytes = requests.get(url_gsheet).content
    my_json = req_bytes.decode()
    str = my_json
    exp = r'>.{2,}(.png|.jpg)'
    result = re.search(exp, str).group(0)
    result = result[1:]
    # start_index = my_json.find('?dl=0">')
    # finish_index = my_json.find('</a>')
    file_name = result
    metadata, f = dbx.files_download('/Приложения/Tilda Publishing/' + file_name)
    return f.content
