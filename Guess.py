from random import choice 
from time import sleep
from Tools.colors import Colors

nums = [1,2,3,4,5,6,7,8,9,10] 
Yellow,Red,Mangeta,Resett,Blue = Colors.Font_Color('Yellow'), Colors.Font_Color("Red"), Colors.Font_Color("Mangeta"), Colors.Font_Color('Reset'), Colors.Font_Color('Blue')
print(Mangeta,'I gonna choice a number between: ',Yellow)

for c in range(1,11):
    print(c,end=' ')

lastcp = 0 
Start = True
print('\n',"-_-_-"*10)
while Start: 
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
    
    
    