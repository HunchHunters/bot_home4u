import random
import re
def random_choice(listMemes, listMusic):
    MemesGen = ListIterator(listMemes)
    MusicGen = ListIterator(listMusic)
    meme_match, song_match = next(MemesGen), next(MusicGen)
    return meme_match, song_match

class ListIterator:
    def __init__(self, list_iter):
        self.list = list_iter
        self.limit = len(list_iter)
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            index = self.counter
            self.counter += 1
            return self.list[index]
        else:
            raise StopIteration


a = ListIterator([1,2,3])
b = ListIterator(['a','b','c'])
#
# # print(next(a), next(b))
# # print(next(a), next(b))
# # print(next(a), next(b))
# print(random.choice([next(a), next(b)]))
# print(random.choice([next(a), next(b)]))
# print(random.choice([next(a), next(b)]))

str = 'File name: <b>photo_2021-08-30_14-56-28_tilda6694466.jpg</b>'
exp = r'>.{2,}(.png|.jpg)'

result = re.search(exp, str).group(0)
# start_index = my_json.find('?dl=0">')
# finish_index = my_json.find('</a>')
file_name = result[1:]
print(file_name)
