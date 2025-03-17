'''
Estructura del control if
Se utiliza para tomar decisiones en expresiones condicionales
'''
#ejemplo 1: if simple
edad = int(input("Ingresa tu edad:"))
documento= input("Tienes documento? (si/no)")
#Condicional: si la edad es mayor o igual a 18
if edad >= 18 and documento=='si':
    #codigo para cuando es mayor a 18
    print ("Eres mayor de edad, puedes votar")
else : 
    #codigo para cuando es menor a 18
    print ("Eres menor de edad o tu documento no es valido, no puedes votar")
print ("fin del programa")