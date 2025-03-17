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

#Ejemplo 6: Operadores aritméticos, relacionales y lógicos  
y = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2
print ("6. El resultado de operar con operadores aritméticos, relacionales y lógicos es:" ,y)

#Ejemplo 7: Con paréntesis
y = (3 + 5) * (2 > 3) and 4 == 4 or not 3 < 2
print ("7. El resultado de operar todo lo anterior con paréntesis:" ,y)

#Ejemplo 8: Todo junto
y = 4**2 * 3 < 6 / (7 - 5) and 7 * 2 + 1 == 14 or not 3 + 5 < 2
print ("8. El resultado de operar todo junto es:" ,y)



