i = 0
impar = []
par = []
while i < 15:
    num = int(input())
    if num % 2 == 0: par.append(num)
    else: impar.append(num)
    if len(par) == 5:
        for k in range(len(par)): print("par[{}] = {}".format(k, par[k]))
        par = []
    elif len(impar) == 5:
        for k in range(len(impar)): print("impar[{}] = {}".format(k, impar[k]))
        impar = []
    i += 1
for k in range(len(impar)): print("impar[{}] = {}".format(k, impar[k]))
for k in range(len(par)): print("par[{}] = {}".format(k, par[k]))