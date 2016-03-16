while True:
    num = input()
    if num == '-1': break
    if 'x' in num:
        print(int(num,16))
    else: print('0x' + hex(int(num))[2:].upper())
