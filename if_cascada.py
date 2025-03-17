'''
if en cascada:
    Estructura de control que permite evaluar varias condiciones, es decir
    si la primera condicion no se cumple, se evalúa la siguiente.
    y asi sucesivamente.
'''
# Ejemplo 1:
#Modificar el programa de votación para que considere la edad de 17 años
edad = int(input("ingrese su edad:"))

if  edad > 18:
    print ("Puede votar")
elif edad == 18:
    print ("¡Es tu primera vez votando!, ya tienes contraseña")
elif edad < 10 :
    print ("No puedes votar, eres un nene")
elif edad == 17:
    print ("Puedes votar el proximo año")
elif edad < 17:
    print ("No puedes votar aún")

