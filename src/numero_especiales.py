
def sumaParesimpares(numInicial, numFinal):
    for numero in range(numInicial, numFinal + 1):
        if numInicial % 2 == 0:
            if parImpar.lower() == "pares" and numero % 2 == 0:
                suma += numero
            elif parImpar.lower() == "impares" and numero % 2 != 0:
                suma += numero
        numInicial += 1
    return suma

if __name__ == "__main__":
    # Entrda
    suma = 0
    contador = 0
    listaNumeros = []
    numInicial = int(input("Ingrese el número inicial: "))
    numFinal = int(input("Ingrese el número final: "))
    parImpar = input("¿Deseas calcular la suma de pares o impares?: ")
    # Proceso
    resultado = sumaParesimpares(numInicial, numFinal)
    # Salida
    print("La suma de los números pares que no son múltiplos de 3 en el rango de 10 a 20 es: ", resultado)