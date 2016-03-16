'''def jos(size, rate):
    if size == 1: return 1
    else: return((jos(size - 1, rate) + rate - 1) % size + 1)

def jp(c, k):
    print("Case {}: {}".format(c,k))
if __name__== "__main__":
    casos = int(input())
    for x in range(casos):
        tam, rat = input().split()
        jp(x + 1, jos(int(tam)*1.0, int(rat)*1.0))
'''
casos = int(input())
for k in range(casos):
    size, rate = input().split()
    size = int(size)
    rate = int(rate)
    for i in range(size):
        x = rate * (i+1)
        while x > size:
            x = ((rate * (x - size) - 1) / (rate - 1))
    print("Case {}: {}".format(k+1, int(x)))

