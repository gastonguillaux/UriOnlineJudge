def VerficaSeDa(quant, lav, sec):
    if quant > lav[0] and quant > lav[1]:
        return print("impossivel")
    if quant > sec[0] and quant > sec[1]:
        return print("impossivel")
    return print("possivel") 

if __name__ == "__main__":
    quantidade = int(input())
    
    lavadora = input().split()
    lavadora = [int(i) for i in lavadora]
    
    secadora = input().split()
    secadora = [int(i) for i in secadora]
    VerficaSeDa(quantidade, lavadora, secadora)