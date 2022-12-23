
k = int(input("Ввидите кол-во циклов"))
i = 0

while i < k:
    n = int(input("Первое число"))
    m = int(input("Второе число"))
    d = 19*m + (n + 239)*(n + 366) / 2
    print(d)
    i += 1
