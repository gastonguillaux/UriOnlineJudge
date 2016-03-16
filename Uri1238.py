casos = int(input())

def maior(a, b):
    if len(a) > len(b): return a
    else: return b

def menor(a, b):
    if len(a) < len(b): return a
    else: return b

for x in range(casos):
    str1, str2 = input().split()
    resto = ""
    
    if len(str1) != len(str2): resto += maior(str1, str2)[-(len(maior(str1,str2)) - len(menor(str1, str2))) :]
    res = ""
    
    for i in range(len(menor(str1, str2))):
        res += str1[i]
        res += str2[i]
    res += resto
    
    print(res)
    