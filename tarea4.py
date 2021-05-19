import matplotlib.pyplot as plt # Imprimir resultados
import matlab.engine # Conectar con matlab
import pygad # Red evolutiva
import numpy as np # Trabajar con matrices
import random # Generar número aleatorios
import math # Hacer operaciones matemáticas

# Se conecta con el entorno de matlab
eng = matlab.engine.start_matlab()

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
    t = np.linspace(0, 10, 1000)

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

# Número máximo de iteraciones o de generaciones
num_generations = 300

# Número de soluciones a ser seleccionados como padres
num_parents_mating = 50

# Función objetiva definida anteriormente que debe tener dos parámetros de entrada
fitness_func = funcCalidad

# Número de poblaciones
#sol_per_pop = 200

# Número de genes en cada cromosoma
num_genes = 15

# Tipo de genes
# types: int, float, and numpy.int/uint/float(8-64)
#gene_type = float

# Rango más bajo de los alelos
#init_range_low = 0

# Rango más alto de los alelos
#init_range_high = 100

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
#"single_point" (for single-point crossover)
#"two_points" (for two points crossover)
#"uniform" (for uniform crossover)
#"scattered" (for scattered crossover)
crossover_type = "uniform"

# Tipo de mutación
#"random" (for random mutation)
#"swap" (for swap mutation)
#"inversion" (for inversion mutation)
#"scramble" (for scramble mutation)
#"adaptive" (for adaptive mutation)
mutation_type = "random"

mutation_probability=0.15

# No permite genes duplicados
allow_duplicate_genes = False

on_generation = stopFunction

filename = 'Final'
# Se carga uno anteriormente creado
load_ga_instance = pygad.load(filename=filename)

# Población inicial
initial_population = load_ga_instance.population

ga_instance = pygad.GA(initial_population=initial_population,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       #sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       #gene_type=gene_type,
                       #init_range_low=init_range_low,
                       #init_range_high=init_range_high,
                       keep_parents=keep_parents,
                       parent_selection_type=parent_selection_type,
                       mutation_probability=mutation_probability,
                       crossover_type=crossover_type,
                       allow_duplicate_genes=allow_duplicate_genes,
                       on_generation=on_generation)

#ga_instance.run()

#ga_instance.plot_result()

solution, solution_fitness, solution_idx = load_ga_instance.best_solution()
print("Mejor individuo del evolutivo: {solution} ".format(solution=solution))
print("Calidad de la mejor solución = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Índice de la mejor solución: {solution_idx}".format(solution_idx=solution_idx))

# Se guarda el resultado del entrenamiento
#filename = 'genetic'
#ga_instance.save(filename=filename)

imprimirResultado(solution)
