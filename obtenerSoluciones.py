import matplotlib.pyplot as plt # Imprimir resultados
import matlab.engine # Conectar con matlab
import pygad # Red evolutiva
import numpy as np # Trabajar con matrices
import random # Generar número aleatorios
import math # Hacer operaciones matemáticas

# Se conecta con el entorno de matlab
eng = matlab.engine.start_matlab()

'''
El cromosoma está definido por:
X = (A1, A2, A3, B1, B2, B3, C1, C2, C3, F1, F2, D2, K1, K2, K3)
'''

# Se define la función objetiva
def funcCalidad(solution, solution_idx):
    # Se selecciona cada valor del cromosoma
    A1 = float(solution[0])
    A2 = float(solution[1])
    A3 = float(solution[2])
    B1 = float(solution[3])
    B2 = float(solution[4])
    B3 = float(solution[5])
    C1 = float(solution[6])
    C2 = float(solution[7])
    C3 = float(solution[8])
    F1 = float(solution[9])
    F2 = float(solution[10])
    D2 = float(solution[11])
    K1 = float(solution[12])
    K2 = float(solution[13])
    K3 = float(solution[14])

    # Se llama a la función de matlab para realizar la operación de la función objetiva
    salida = eng.funcObjetiva(A1,A2,A3,B1,B2,B3,C1,C2,C3,D2,F1,F2,K1,K2,K3)

    # Se retorna el valor de la función objetiva
    return -salida

def imprimirResultado(solution):
    # Se selecciona cada valor del cromosoma
    A1 = float(solution[0])
    A2 = float(solution[1])
    A3 = float(solution[2])
    B1 = float(solution[3])
    B2 = float(solution[4])
    B3 = float(solution[5])
    C1 = float(solution[6])
    C2 = float(solution[7])
    C3 = float(solution[8])
    F1 = float(solution[9])
    F2 = float(solution[10])
    D2 = float(solution[11])
    K1 = float(solution[12])
    K2 = float(solution[13])
    K3 = float(solution[14])

    # Se obtiene el array con los valores de salida
    y = eng.graficar(A1,A2,A3,B1,B2,B3,C1,C2,C3,D2,F1,F2,K1,K2,K3)

    # Se crea un espacio lineal con los valores del tiempo
    t = np.linspace(0, 100, 1000)

    # Se cambia el tipo de dato a un arreglo numpy
    y = np.array(y)

    # Se imprimen los resultados
    plt.plot(t, y)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Salida")
    plt.grid()
    plt.show()

# Función para detener el entrenamiento
def stopFunction(instance):
    # Se obtiene la calidad de la mejor solución
    fit = instance.best_solution()[1]
    # Se obtiene el índice de la mejor solución
    index = instance.best_solution()[2]
    print(instance.generations_completed, "Mejor solución: {fit}".format(fit=fit), index)
    # Condición de parada
    if fit >= -0.5:
        return "stop"

filename = 'Final'
# Se carga uno anteriormente creado
load_ga_instance = pygad.load(filename=filename)

poblacion = load_ga_instance.population

# Se obtiene la mejor solución de la población
solution, solution_fitness, solution_idx = load_ga_instance.best_solution()
print("Mejor individuo del evolutivo: {solution} ".format(solution=solution))
print("Calidad de la mejor solución = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Índice de la mejor solución: {solution_idx}".format(solution_idx=solution_idx))

# Se imprimen los cuatro mejores resultados
for i in range(4):
    print(solution, solution_fitness)
    imprimirResultado(solution)
    poblacion = np.delete(poblacion, solution_idx, axis=0)
    temp = []
    for j in range(len(poblacion)):
        temp.append(funcCalidad(poblacion[j], 0))
    solution_fitness = np.nanmax(temp)
    solution_idx = np.where(solution_fitness == temp)
    solution = poblacion[solution_idx]
    solution = solution[0]
