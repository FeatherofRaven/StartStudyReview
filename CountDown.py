from time import localtime, sleep

def tymer(tuple):
    string = ''
    for v in tuple: 
        string += str(v)
        if len(string) > 1 and len(string) < 3:
            string += ':'
    return string

while True:  
    try: 
        set_type = str(input("{hour):{minute) (second) chose:(h,m,s): "))
        set_timer = int(input("Time in (h):(m):(s}: ")) 
    except ValueError or NameError or len(set_type)>1: 
        print('ERROR\n')

    finally:
        local_time = localtime()
        local_time = local_time[3:5]
        print(f"Local Time:{tymer(local_time)}")

    if set_type == 's': 
        sleep(set_timer)
        local_time = localtime()
        local_time = local_time[3:5]
        print(f"End Time -> {tymer(local_time)}")

    if set_type == 'm': 
        set_timer *= 60 
        sleep(set_timer)
        local_time = localtime()
        local_time = local_time[3:5]
        print(f"End Time -> {tymer(local_time)}")    

    if set_type == 'h': 
        set_timer *= 60 * 60
        sleep(set_timer)
        local_time = localtime()
        local_time = local_time[3:5]
        print(f"End Time -> {tymer(local_time)}")