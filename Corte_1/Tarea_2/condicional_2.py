precio = int (input ("Ingrese un valor: "))

if precio <= 1000 :
    print ("Barato")
elif precio > 1000 and precio <= 2000 :
    print ("Medianamente Barato")
elif precio > 2000 and precio <= 3000 :
    print ("Medianamente Caro")
else:
    print ("Caro")
