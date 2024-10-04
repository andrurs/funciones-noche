# Ejemplos de argumentos predeterminados


def my_function(country="Colombia"):
    print("I am from " + country)

#invocar
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Argumento arbitrario (*args)------------------------------------------
def mostrarEstudiantes(*args):
    print("\nEl estudiante: " + args[2])

mostrarEstudiantes("Email","Tobias","Linus")

# Argumentos de palabras clave ---------------------------------
def mostrarCarros(carro1,carro2,carro3):
    print("\nEl carro es: " + carro2)

mostrarCarros(carro1="BMW",carro3="Ferrari",carro2="Ford")

#si son muchos datos existe el argumento **kwargs
def mostrarCliente(**kwargs):
    print("\nSu apellido es: " + kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido = "Montenegro")