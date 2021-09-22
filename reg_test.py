import re

exp = r'>\w{1,}.jpg'

?dl=0">IvanAnisimovPhoto_tilda6653614.png


result = re.search(exp, 'hui.jpg')

print(result)
