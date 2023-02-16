i = 0 #Количество выполненных операций
deistv = ""#Для действия
otvet =0.0#Для ответа

print("Введите количество операций")
oper = int(input())

print("Введите первое число")
chislo1 = float(input())

print("Введите второе число")
chislo2 = float(input())

print("Введите операцию")
deistv = input()
if(deistv == "+"):
        otvet = chislo1 + chislo2
        print(f"{otvet}")
elif(deistv == "-"):
        otvet = chislo1 - chislo2
        print(f"{otvet}")
elif(deistv == "*"):
        otvet = chislo1 * chislo2
        print(f"{otvet}")
elif(deistv == "/"):
        otvet = chislo1 / chislo2
        print(f"{otvet}")
elif(deistv == "step"):
        otvet = chislo1**chislo2
        print(f"{otvet}")
elif(deistv == "%"):
        otvet = chislo1 % chislo2
        print(f"{otvet}")

while(i != oper-1):
    print("Введите второе число")
    chislo2 = float(input())
    print("Введите операцию")
    deistv = input()
    if(deistv == "+"):
        otvet = otvet + chislo2
        print(f"{otvet}")
    elif(deistv == "-"):
        otvet = otvet - chislo2
        print(f"{otvet}")
    elif(deistv == "*"):
        otvet = otvet * chislo2
        print(f"{otvet}")
    elif(deistv == "/"):
        if(chislo2 == 0):
            print(f"деление на ноль не возможно")
            i = i + 1
        else:
            otvet = otvet / chislo2
            print(f"{otvet}")
            
    elif(deistv == "step"):
        otvet = otvet**chislo2
        print(f"{otvet}")
    elif(deistv == "%"):
        otvet = otvet % chislo2
        print(f"{otvet}")
    i = i+1



   




