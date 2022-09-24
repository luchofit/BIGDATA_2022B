print("Hola mundo") #string cadena de caracteres
Frase = "hola mundo"
print(Frase)

#Variables
#5.0 es una variable tipo float
# 3 es una variable tipo int
# hola es una variable tipo str
# False/True es una variable de tipo bool

#Función implicita
# round (redondeo flotantes)

Ejemplo = round(6.4)
print(Ejemplo)

#Debería imprimir 6

#operación entre variables númericas
x = 1
y = 2
print("suma:", x+y)
print("Resta:", x-y)
print("división:", x/y)
print("potencia:", x**y)
print("modulo:", x%y)

#LOOPS (iteraciones/condicionales)

for num in range (0,10):
    print(num)
    if num % 3 == 0:
        print(num)
        break
    else:
        continue
# (0 (comienza), 10 (finaliza en 9), 1 (que aumente de a uno))

# Operaciones con strings

Frase2 = "Big Data"
print(Frase + Frase2)

n_repeticiones = 10
print(n_repeticiones * Frase)