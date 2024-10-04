#Ejemplo para calcular el area del triangulo

#entradas
base = int(input("Ingrese la base del triangulo: "))
altura = int(input("Ingrese la altura del triangulo: "))

#proceso
def calculaAreaTriangle(a,b):
    area=(a*b)/2
    #print("El area del triangulo es: ",area)
    return area
resultado = calculaAreaTriangle(base,altura)
print("El area del triangulo es: ", resultado)