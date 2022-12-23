
while True:
    c= input("Включить калькулятор: ").lower()
    if c == "нет":
        break
    x = int(input("Ввидите число "))
    y = int(input("Ввидите число "))
    z = input("Ввидите (+, -, /, *) ")
    if z == "+":
        print(x+y)
    elif z == "-":
        print(x-y)
    elif z == "*":
        print(x*y)
    elif z == "/":
        if y == 0:
            print("делить на ноль нельзя")
        else:
            print(x/y)
    else:
        print("Вы ввели неправильный символ")
