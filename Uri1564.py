
if __name__ == "__main__":
    try:
        while True:
            prot = int(input())
            if prot == 0:
                print("vai ter copa!")
            else:
                print("vai ter duas!")
    except EOFError:
        pass