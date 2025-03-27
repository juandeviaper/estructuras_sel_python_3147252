'''
Escribir un programa que calcule el salario neto de un trabajador después de descuentos
y bonificaciones.
=> Inicialmente, el programa debe solicitar un tipo de trabajador entre los siguientes: 
a - Contrato a termino indefinido
b - Contrato por prestación de servicios
c - Contrato de aprendizaje
d - Jornal
=> Jornal: 
Se debe solicitar:
- el tipo de unidad a pagar 
- el numero de unidades hechas 
- el valor de la unidad
el salaio neto se calcula como
el valor_unidad * numero_unidades
si el numero de unidades es mayor a 100 se le da una bonificacion del 10%

=> Contrato de aprendizaje
se debe solicitar el salario minimo 
el salario neto es 
el  75% del salario minimo

=> Contrato de prestacion de servicio
se debe solicitar
- el valor del contrato
-el numero de meses trabajados
-antiguedad en la empresa

Se calcula dividiendo el valor del contrato entre el numero de meses trabajados
-Si la antiguedad es menor a 2 años 
se le aumenta el 2% al salario mensual 
-Si la antiguedad esta entre 2 y 5 años 
se le aumenta el 5% al salario mensual
-Si la antiguedad es mayor a 5 años
se le aumenta el 10% al salario mensual

Descuentos de ley
- 8% de salud
- 10% de pension 
- 1% de caja de compensacion

=> contrato a termino indefinido
el salario se calcula con base en la siguiente tabla
de escalafones o grados:

- 1: 1.5 veces el SMLV
- 2: 1.7 veces el SMLV
- 3: 2 veces el SMLV
- 4: 2.5 veces el SMLV
- 5: 3 veces el SMLV
El programa debe solicita el escalafon o grado del empleado

-Las bonificaciones y descuentos de ley son las mismas que en el caso B

'''
#Variable global: Es una variable que puede ser reconocida y asignada en cualquier parte del programa
#NOTA: Se recomienda inicializar (definir y dar valor inicial a las variables globales al principio del programa)
#EJEMPLO: variables para almacenar resultados finales
tipo_empleado = input("Ingrese el tipo de empleado (a/b/c/d): ")

# Inicializar la variable salario_neto
salario_neto = 0

if tipo_empleado == "a":
    print("Ha ingresado contrato a término indefinido")
    SMLV = float(input("Ingrese SMLV: "))
    escalafon = int(input("Ingrese el escalafón (1-5): "))
    antiguedad = int(input("Ingrese la antigüedad en la empresa (en años): "))
    
    # Calcular salario mensual según el escalafón
    if escalafon == 1:
        salario_mensual = 1.5 * SMLV
    elif escalafon == 2:
        salario_mensual = 1.7 * SMLV
    elif escalafon == 3:
        salario_mensual = 2 * SMLV
    elif escalafon == 4:
        salario_mensual = 2.5 * SMLV
    elif escalafon == 5:
        salario_mensual = 3 * SMLV    
    else:
        print("Escalafón no válido")
        salario_mensual = 0

    
     # Bonificaciones
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif 2 <= antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    else:  # antigüedad > 5
        bonificacion = salario_mensual * 0.10
        
    # Descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    
    # Calcular salario neto
    salario_neto = salario_mensual - (descuento_salud + descuento_pension + descuento_caja)
    

    

elif tipo_empleado == "b":
    print("Ha ingresado contrato por prestación de servicios")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese el número de meses trabajados: "))
    antiguedad = int(input("Ingrese la antigüedad en la empresa (en años): "))
    
    salario_mensual = valor_contrato / numero_meses
    
    # Bonificaciones
    if antiguedad < 2:
        bonificacion = salario_mensual * 0.02
    elif 2 <= antiguedad <= 5:
        bonificacion = salario_mensual * 0.05
    else:  # antigüedad > 5
        bonificacion = salario_mensual * 0.10
    
    # Refactorización
    salario_mensual += bonificacion
    
    # Descuentos
    descuento_salud = salario_mensual * 0.08
    descuento_pension = salario_mensual * 0.10
    descuento_caja = salario_mensual * 0.01
    
    # Calcular salario neto
    salario_neto = salario_mensual - (descuento_salud + descuento_pension + descuento_caja)

elif tipo_empleado == "c":
    print("Ha ingresado contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el salario mínimo: "))
    salario_neto = salario_minimo * 0.75  # 75% del salario mínimo

elif tipo_empleado == "d":
    print("Ha ingresado jornal")
    tipo_unidad = input("Ingrese el tipo de unidad: ")
    numero_unidades = int(input("Ingrese el número de " + tipo_unidad + " hechas: "))
    valor_unidad = float(input("Ingrese el valor de " + tipo_unidad + ": "))
    
    salario_neto = numero_unidades * valor_unidad
    
    # Bonificación si el número de unidades es mayor a 100
    if numero_unidades > 100:
        bonificacion = salario_neto * 0.10
        salario_neto += bonificacion

else:
    print("Tipo de empleado no válido")

# Mostrar el salario neto
print("El salario neto es:", salario_neto)
print("Fin del programa")