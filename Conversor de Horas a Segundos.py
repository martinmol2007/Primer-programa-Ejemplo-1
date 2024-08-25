print ("Bienvenido a mi conversor de horas a segundos!")

horas = float(input("Inroduce el numero de horas que deseas convertir a segundos:"))
segundos = horas * 3600

if horas <= 1:
    print (str(horas) + " hora son " + str(segundos) + " segundos ")
else:
    print(str(horas) + " horas son " + str(segundos) + " segundos ")
