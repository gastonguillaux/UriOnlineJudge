try:
    while True:
        texto = input()
        bold = 0
        it = 0
        
        i = ['<i>', '</i>']
        b = ['<b>', '</b>']
        
        res = ''
        
        for k in range(len(texto)):
            if texto[k] == '_' and it % 2 == 0:
                res += i[it]
                it += 1
            elif texto[k] == '_' and it % 2 == 1:
                res += i[it]
                it += 0                
            elif texto[k] == '*' and bold % 2 == 0:
                res += b[bold]
                bold += 1
            elif texto[k] == '*' and bold % 2 == 1:
                res += b[bold]
                bold += 0
            else:
                res += texto[k]
        print(res)            
        
except EOFError:
    pass