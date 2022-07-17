from hashlib import new
from random import choices 

with open('wordsrandom.txt') as file_open:
    file = file_open.read() 
    word = ''
    words = list()
    for l in file:
        if l == '\n' and word not in words:
            words.append(word.strip())
            word = ''
        if str(l).isalpha and l != '\n':
            word += l




    print(words)


ch = choices(words,k= 10)
new_words = ''
for w in ch: 
    new_words += f"'{w}', "


print('\n',new_words.strip())
