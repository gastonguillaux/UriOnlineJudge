
if __name__ == "__main__":
    try:
        while True:
            angulo = int(input())
            if (angulo % 6 == 0):
                print('Y')
            else:
                print('N')
    except EOFError:
        pass