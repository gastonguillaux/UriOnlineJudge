from pprint import pprint
cadeia_alimentar = {
                    "vertebrado": {
                        "ave":{
                            "carnivoro": "aguia",
                            "onivoro": "pomba"
                        },
                        "mamifero":{
                            "onivoro": "homem",
                            "herbivoro": "vaca"
                        }
                    },
                    "invertebrado":{
                        "inseto":{
                            "hematofago": "pulga",
                            "herbivoro": "lagarta"
                        },
                        "anelideo":{
                            "hematofago": "sanguessuga",
                            "onivoro": "minhoca"
                        }
                    }

                   }

try:
    while True:
        a = input()
        b = input()
        c = input()
        print(cadeia_alimentar[a][b][c])
except EOFError:
    pass