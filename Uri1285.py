try:
    while True:
        a, b = input().split()
        nums = 0
        for x in range(int(a), int(b) + 1, 1):
            auxStr = str(x)
            unNum = set(auxStr)
            if len(unNum) == len(auxStr): nums += 1
        print(nums)
except EOFError:
    pass