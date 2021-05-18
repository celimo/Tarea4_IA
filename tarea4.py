import matplotlib.pyplot as plt
import matlab.engine
import pygad
import numpy as np
import random
import math

# Se conecta con el entorno de matlab
eng = matlab.engine.start_matlab()

# Se define la función objetiva
def funcCalidad(solution, solution_idx):
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

    salida = eng.funcObjetiva(A1,A2,A3,B1,B2,B3,C1,C2,C3,D2,F1,F2,K1,K2,K3)

    return -salida

def imprimirResultado(solution):
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

    y = eng.graficar(A1,A2,A3,B1,B2,B3,C1,C2,C3,D2,F1,F2,K1,K2,K3)

    t = np.linspace(0, 100, 1000)

    y = np.array(y)

    print(y.shape)
    plt.plot(t, y)
    plt.show()

# Función para detener el entrenamiento
def stopFunction(instance):
    fit = instance.best_solution()[1]
    index = instance.best_solution()[2]
    print("Mejor solución: {fit}".format(fit=fit), index)
    if fit >= -2:
        return "stop"

# Número máximo de iteraciones o de generaciones
num_generations = 500

# Número de soluciones a ser seleccionados como padres
num_parents_mating = 20

# Función objetiva definida anteriormente que debe tener dos parámetros de entrada
fitness_func = funcCalidad

# Número de poblaciones
sol_per_pop = 50

# Número de genes en cada cromosoma
num_genes = 15

# Rango más bajo de los alelos
init_range_low = 0.00001

# Rango más alto de los alelos
init_range_high = 5

# Numero de padres que se quedan (-1=todos, default)
keep_parents = 5

# Tipo de selección de padres
'''
"sss"(for steady-state selection)
'"rws"(for roulette wheel selection)
"sus"(for stochastic universal selection)
"rank"(for rank selection)
"random"(for random selection)
"tournament"(for tournament selection)
'''
parent_selection_type = "tournament"

# Operaciones de cruce genético
crossover_type = "uniform"

# Tipo de mutación
mutation_type="random"

mutation_probability=0.25

# No permite genes duplicados
allow_duplicate_genes = False

on_generation = stopFunction

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       init_range_low=init_range_low,
                       init_range_high=init_range_high,
                       keep_parents=keep_parents,
                       parent_selection_type=parent_selection_type,
                       mutation_probability=mutation_probability,
                       crossover_type=crossover_type,
                       allow_duplicate_genes=allow_duplicate_genes,
                       on_generation=on_generation)

ga_instance.run()

ga_instance.plot_result()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Mejor individuo del evolutivo: {solution} ".format(solution=solution))
print("Calidad de la mejor solución = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Índice de la mejor solución: {solution_idx}".format(solution_idx=solution_idx))

# Se guarda el resultado del entrenamiento
filename = 'genetic'
ga_instance.save(filename=filename)

imprimirResultado(solution)
