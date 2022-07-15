from random import choice 
from time import sleep


# Font
def Font_Color(cor):
    Color_Font ={"Black":'\033[1;30m', "Red":'\033[1;31m', 'Green':'\033[1;32m', 'Yellow':'\033[1;33m', 'Blue':'\033[1;34m', 'Mangeta':'\033[1;35m', 'Cyan':'\033[1;36m', 'Light_Gray':'\033[1;37m', 'Dark_Gray':'\033[1;90m', 'Light_Red':'\033[1;91m', 'Light_Green':'\033[1;92m', 'Light_Yellow':'\033[1;93m', 'Light_Blue':'\033[1;94m', 'Light_Mangeta':'\033[1;95,m', 'Light_Cyan':'\033[1;96m', 'White':'\033[1;97m', 'Bold':'\033[;1m', 'Reverse' : '\033[;7m', 'Reset':'\033[0;0m'}
    return Color_Font[f"{cor}"]
    

# Background 
def Background_Color(cor): 
    Color_Background ={"Black":'\033[1;40m', "Red":'\033[1;41m', 'Green':'\033[1;42m', 'Yellow':'\033[1;43m', 'Blue':'\033[1;44m', 'Mangeta':'\033[1;45m', 'Cyan':'\033[1;46m', 'Light_Grey':'\033[1;47m', 'Dark_Grey':'\033[1;100m', 'Light_Red':'\033[1;101m', 'Light_Green':'\033[1;102m', 'Light_Yellow':'\033[1;103m', 'Light_Blue':'\033[1;104m', 'Light_Mangeta':'\033[1;105,m', 'Light_Cyan':'\033[1;106m', 'White':'\033[1;107m'}
    return Color_Background[f"{cor}"]


Yellow,Red,Mangeta,Resett,Blue = Font_Color('Yellow'), Font_Color("Red"), Font_Color("Mangeta"), Font_Color('Reset'), Font_Color('Blue')
print(Mangeta,'I gonna choice a number between: ',Yellow)

for c in range(1,11):
    print(c,end=' ')


nums = [1,2,3,4,5,6,7,8,9,10] 
lastcp = 0 
Start = True

while Start:
    print('\n',"-_-_-"*10) 
    try: 
        user = int(input(f'{Blue}Choice a Number (1 to 10),(0 to exit): ')) 
        if user == 0: 
            print(f"{Mangeta}BYE BYE! COME BACK SOON!! <ô>_<ô>{Resett}")
            Start = False
            break
        try:
            cp = choice(nums)
            if cp == user: 
                print(f"{Yellow} Congratulations, i was thinking about this {cp}!!! {Resett}")
            

            if cp != user and user > 0:
                print(f'{Red} {user} not is {cp}!, try again ^_^ {Resett}')
                
        except cp == lastcp or NameError or type(user) == str :
            pass 

    except ValueError:
        print(f'{Red}\n!-!-!-!You Made a Mistake!-!-!-!\n{Resett}')
    
    
    