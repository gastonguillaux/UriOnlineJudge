def f():
    num1, num2 = input().split()
    num1, num2 = int(num1), int(num2)
    if num1 < num2:
        if num2 <= 2: return print("nova\n")
        if num2 <= 96: return  print("crescente\n")
        if num2 <= 100: return print("cheia\n")
    elif num1 > num2:
        if num2 >= 97: return print("cheia\n")
        if num2 >= 3: return print("minguante\n")

if __name__ == "__main__":
        f()
    
        