a = int(input("Ввидите число "))
b = int(input("Ввидите число "))
c = int(input("Ввидите число "))
if a*b == c:
    print("Возмоно")
elif a*c == b:
    print("Возможно")
elif c*b == a:
    print("Возможно")
else:
    print("Ошибка")
