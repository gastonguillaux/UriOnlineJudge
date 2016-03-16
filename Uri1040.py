try:
    while True:
        notas = [float(i) for i in input().split()]
        n1, n2, n3, n4 = notas
        media = [n1 * 0.2, n2 * 0.3, n3 * 0.4, n4 * 0.1]
        print("Media: {}".format(round(sum(media),1)))
        if sum(media) >= 7.0:
            print("Aluno aprovado.")
        elif sum(media) < 5.0:
            print("Aluno reprovado.")
        else:
            print("Aluno em exame.")
            rec = round(float(input()),1)
            print("Nota do exame: {}".format(rec))
            mf = round((sum(media) + rec)/2,1)
            if mf >= 5.0:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
            print("Media final: {}".format(mf))
except EOFError:
    pass