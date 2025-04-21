#loreto vargas
#09-04-2025
#poan con queso

mes = int(input("Introduce el número del mes (1-12): "))

if mes >= 1 and mes <= 3:
    print("invierno")
elif mes >= 4 and mes <= 6:
    print("primavera")  
elif mes >= 7 and mes <= 9:
    print("verano")
elif mes >= 10 and mes <= 12:
    print("otoño")
else:
    print("inválido")