año = int(input("Ingrese un año: "))

if año%4 ==0 and año%100!=0:
    print("Es biciesto")

elif año%100 ==0 and año%400 !=0:
    print("Es biciesto")   

else:
    print("No es biciesto")   