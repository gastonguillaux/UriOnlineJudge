def winner(x,y):
    rafa = ((3*x)**2) + (y**2)
    beto = (2*(x**2)) + ((5*y)**2)
    car = (-100*x) + (y**3)
    if rafa > beto and rafa > car:
        return print("Rafael ganhou")
    elif beto > rafa and beto > car:
        return print("Beto ganhou")
    elif car > rafa and car > beto:
        return print("Carlos ganhou")

if __name__ == "__main__":
    casos = int(input())
    for x in range(casos):
        x, y = input().split()
        winner(int(x), int(y))
        