try:
    while True:
        import locale
        locale.setlocale(locale.LC_ALL,'')
        num = float(input())
        dig = float(input())/100
        num += dig
        print(locale.currency(num, grouping=True))
except EOFError:
    pass