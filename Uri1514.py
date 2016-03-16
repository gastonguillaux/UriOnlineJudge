while True:
    en = [int(i) for i in input().split()]
    if en[0] == en[1] == 0: break
    questions, people = en
    feat = [0,0,0,0]
    applicant = []
    matriz = []

    ResolAll = False
    UmResolveu = False
    ProbAllResol = False
    TodosResolUm = False

    for y in range(people): applicant.append(0)
    for question in range(questions):
        result = [int(i) for i in input().split()]
        matriz.append(result)

    sumAll = 0
    for n in matriz:

