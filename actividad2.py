#Descripción actividad 2
'''
Elabore un programa en Python que determine si usted puede casarse
a)casarse
b)comprometerse
c)QUEDARSE SOLTERO
con base en las siguientes características(variables)
-Estado civil (strig = "soltero", "casado", "comprometido")
-Edad(int)
-temperamento(string= "buena persona", "mala persona")
-Fisico(string = lindo, linda)
'''
estado_civil = input("Ingresa su estado civil (soltero/casado/comprometido)")
edad = int(input("Ingresa su edad:"))
temperamento = input("Ingresa su temperamento (buena persona/mala persona)")
fisico = input("Ingresa el fisico: (lindo/a / feo/a)")
salario =int(input("Ingresa su salario:"))

if estado_civil == "casado" or estado_civil == "comprometido":
    print("No puedes acercarte a esa persona")
elif edad < 18:
    print("No puedes acercarte a esa persona, porque no tienes la edad suficiente")
elif temperamento == "mala persona":
    print ("No puedes acercarte a esa persona, te generaría estres")
elif fisico == "feo":
    print("No puedes acercarte a esa persona, no te atrae fisicamente")
elif salario < 2000000:
    print("No puedes acercarte a esa persona, es pobre")
else :
    print("Puedes casarte con esa persona")
print("Fin del programa")