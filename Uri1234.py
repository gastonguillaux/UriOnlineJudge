try:
    while True:
        msg = input()
        car = 0
        msg2 = ""
        for x in range(len(msg)):
            if msg[x] != " ":
                if car == 0 or car % 2 == 0:
                    msg2 += msg[x].upper()
                    car += 1 
                else:
                    msg2 += msg[x].lower()
                    car += 1
        
            if msg[x] == " ":
                msg2 += msg[x]
        print(msg2)
except EOFError:
    pass