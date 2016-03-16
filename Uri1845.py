while True:
    try:
        letras = 'sjbvxpz'
        texto = input()
        for x in texto:
            if x in letras:
                texto = texto.replace(x, 'f')
            elif (x in letras.upper()):
                texto = texto.replace(x, 'F')
        while ('ff' in texto) or ('Ff' in texto) or ('FF' in texto) or ('fF' in texto):
            texto = texto.replace('Ff', 'F')
            texto = texto.replace('FF', 'F')
            texto = texto.replace('fF', 'F')
            texto = texto.replace('ff', 'f')
        print(texto)
    except EOFError:
        pass