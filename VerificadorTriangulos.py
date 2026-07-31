# App de consola
# Ingreso de datos
ladoA = float(input("Ingrese el lado A del triangulo: "))
ladoB = float(input("Ingrese el lado B del triangulo: "))
ladoC = float(input("Ingrese el lado C del triangulo: "))

# Verificar si los lados forman un triángulo
if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):

    if ladoA == ladoB == ladoC:
        print("Resultado: El triángulo es Equilátero.")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("Resultado: El triángulo es Isósceles.")
    else:
        print("Resultado: El triángulo es Escaleno.")

else:
    print(" Los valores ingresados no forman un triángulo.")