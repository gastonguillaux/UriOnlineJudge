while True:
    entrada = [int(x) for x in input().split()]
    if len(entrada) == 1 and entrada[0] == 0: break
    v1 = entrada[0]
    v2 = entrada[2]
    economia = entrada[1]
    dias = (economia * v2) / (v2-v1)
    paginas = int(v1* dias)
    if paginas == 1:
        print("{0} pagina".format(paginas))
    else:
        print("{0} paginas".format(paginas))