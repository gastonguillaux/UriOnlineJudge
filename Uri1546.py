
def main():
    resolvers = {1:"Rolien",2:"Naej",3:"Elehcim",4:"Odranoel"}
    vezes = int(input())
    for i in range(vezes):
        mensagens = int(input())
        for k in range(mensagens):
            indice = int(input())
            print(resolvers[indice])


if __name__ = "__main__": main()
    