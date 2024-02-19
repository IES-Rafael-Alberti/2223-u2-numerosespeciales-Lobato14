from src. numero_especiales import sumaParesimpares

def test_calcular_suma_pares_no_multiplos_de_3():
    assert sumaParesimpares.calcular_suma_pares_no_multiplos_de_3(10, 20) == 72
    assert sumaParesimpares.calcular_suma_pares_no_multiplos_de_3(20, 30) == 110
    assert sumaParesimpares.calcular_suma_pares_no_multiplos_de_3(30, 40) == 150

def test_calcular_suma_impares_no_multiplos_de_3():
    assert sumaParesimpares.calcular_suma_impares_no_multiplos_de_3(10, 20) == 60
    assert sumaParesimpares.calcular_suma_impares_no_multiplos_de_3(20, 30) == 65
    assert sumaParesimpares.calcular_suma_impares_no_multiplos_de_3(30, 40) == 75
