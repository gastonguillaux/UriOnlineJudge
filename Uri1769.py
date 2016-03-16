try:
    while True:
        cpf = input().replace(".","").split("-")
        soma = 0
        digito = ""
        for j in range(len(cpf[0])):
            soma += (j + 1) * int(cpf[0][j])
        if soma % 11 == 10: digito += str(0)
        else: digito += str(soma % 11)
        soma = 0    
        for j in range(len(cpf[0])):
            soma += (len(cpf[0]) - j) * int(cpf[0][j])
        if soma % 11 == 10: digito += str(0)
        else: digito += str(soma % 11)
        if digito == cpf[1]: print("CPF valido")
        else: print("CPF invalido")
except EOFError:
    pass