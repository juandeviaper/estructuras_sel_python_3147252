'''
Operadores Lógios
Aquellos quoperan unicamente con los calores booleanos (V-F)
Acorde a tablas de verdad
'''
#Ejemplo 1: Operador not
y= not True
print ("1.El resultado de operar con not es" ,y)

#Ejemplo 2: Operador and
y = False and True
print ("2.El resultado de operar con and es" ,y)

# Ejemplo 3 Operador or 
y = False or True
print ("3.El resultado de operar con or es" ,y)

'''
Jerarquía de precedencia de operadores (lógicos inclusive)
1. ()
2. **
3. * , / , %
4. +, -
5. < , >, <=, >=; !=, ==
6. not
7. and
8. or    
9. =
'''

#Ejemplo 4: Jerarquía de operadores 
y = False and not True or False 
print ("4. El resultado de operar con jerarquía es:" ,y)

#Ejemplo 5: Operadores relacionales y lógicos 
y = not 3 > 4 and 4 == 4 or 3 < 2
print ("5. El resultado de operar con operadores logicos y relacionales es:" ,y)
