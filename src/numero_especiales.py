
def sumaParesimpares(numInicial, nunFinal):
    
    if numInicial and numFinal %3 == 0:
        for numero in range(numInicial, numFinal):
            suma = numero + numero
            contador += 1
    else:
        for numero in range(numInicial, numFinal):
            suma = numero + numero
            contador += 1
    return str(suma)


if __name__ == "__main__":
    # Entrda
    contador = 0
    listaNumeros = []
    numInicial = int(input("Ingrese el número inicial: "))
    numFinal = int(input("Ingrese el número final: "))
    parImpar = input("¿Deseas calcular la suma de pares o impares?: ")
    # Proceso

    # Salida