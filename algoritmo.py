x = int(input("ingrese un número: "))
y = int(input("ingrese un número: "))
z = int(input("ingrese un número: "))

if x>y>z :
    rta = "Este es el mayor de los tres: " + str(x)

else :
    if x>y<z :
        rta ="Este es el mayor de los tres: " + str(z)
    
    else :
        if x<y>z :
           rta = "Este es el mayor de los tres: " + str(y)

print (rta)