def simple_cript(entrada):
    #entrada = entrada.split()
    saida = []
    
    for item in range(len(entrada)):
        for letra in range(len(entrada[item])):
            # MAIUSCULAS
            if entrada[item][letra].isalpha() and ord(entrada[item][letra]) <= 90:
                if ord(entrada[item][letra]) < ord('N'):
                    saida.append(chr(ord(entrada[item][letra])+13))
                else:
                    saida.append(chr(ord(entrada[item][letra])-13))
            
            # MINUSCULAS
            elif entrada[item][letra].isalpha() and ord(entrada[item][letra]) >= 97:
                if ord(entrada[item][letra]) < ord('n'):
                    saida.append(chr(ord(entrada[item][letra])+13))
                else:
                    saida.append(chr(ord(entrada[item][letra])-13))
            
        #DEMAIS CARACTERE S
            else:
                saida.append(entrada[item][letra])
                
    print(''.join(saida))
    
if __name__ == '__main__':
    while (True):
        entrada = input()
        if entrada == '':
            break
        else:
            simple_cript(entrada)