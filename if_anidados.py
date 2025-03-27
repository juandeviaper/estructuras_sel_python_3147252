'''
Los if anidados son estructuras selectivas que se encuentran dentro de otro if
Syntax:
if condicion:
     if condicion:
        bloque de instr
     else:
        if condicion:
            bloque de instr
        else: 
            bloque de instr
else:
    bloque de instruciiones
'''

#Ejemplo 1:
#Modificación del ejercicio de votación, ahora solo puede votar si es mayor de edad pero si tiene documento
#Mostrar explicaciones en los otros casos

edad = int(input("Ingrese su edad:"))
if edad >= 18:
    documento = input("Tiene documento? (si/no):")
    if documento == "si":
        print("Usted puede votar")
    else:
        print("Usted no puede votar")
        print("Porque no tiene documento")
        
else: 
        print("Usted no puede votar")
        print("Porque es menor de edad")