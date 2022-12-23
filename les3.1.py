def summa(x, y, z):
    if z == "+":
        return x+y
    elif z == "-":
        return x-y
    elif z == "*":
        return x*y
    elif z == "/":
        if y == 0:
            print("делить на ноль нельзя")
        else:
            return x/y
    else:
        print("Вы ввели неправильный символ")


try:
    x = int(input("Ввидите число "))
    y = int(input("Ввидите число "))
    z = input("Ввидите (+, -, /, *) ")
    print(summa(x, y, z))
except (ValueError):
    print("Вы ввели не число")
