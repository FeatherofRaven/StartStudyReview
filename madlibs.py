#output is return a default custom message chosen by user [v]
#using a fstrings to get result   [v]
#challenge: the user chose the word and what will be write in the message
#create  a function to confirm links
from Tools.colors import Colors

Red = Colors.Font_Color('Red')
Resett = Colors.Font_Color('Reset')
Blue = Colors.Font_Color('Blue')
Yellow = Colors.Font_Color('Yellow')

ex_message = """Automatic message no reply 
    Hello! We are from {Business@fakemail.com} and recently you singed up on our {FakeSite}. 
    click on this link bellow 
    {linkfaketogetvictim.com}
    <emoji happy> emoji happy""" # 3 variables to be changed in program 

def input_list(text): # Make the inpput recive only the necessery
    list_phrase = []
    phrase, letters = '',''
    while len(list_phrase) < 3 and len(list_phrase) != 3 : 
        var = str(input(text))
        for l in var: 
            if l.isalpha or l.isascii: 
                letters += l
            if l == ' ': 
                phrase = letters
                list_phrase.append(phrase.strip())
                phrase, letters = '', ''
    return list_phrase


print(f"{Red}{ex_message}{Blue}")
fake_contacts =input_list('Email, Website, link: ')

print(f"""{Yellow}Automatic message no reply 
    Hello! We are from {fake_contacts[0]} and recently you singed up on our {fake_contacts[1]}. 
    click on this link bellow 
    {fake_contacts[2]}
    emoji happy emoji happy{Resett}""")
        