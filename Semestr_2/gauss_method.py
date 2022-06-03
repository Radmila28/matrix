import pygad
import numpy

items = ['яблоки', 'бананы', 'зонт', 'наушники', 'ноубук', 'футболка', 'панама', 'дождевик',
         'пуховик', 'камера', 'зачет по питону']
values = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
weights = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]

backpack_limit = 25

gene_space = [0, 1]


def fitness_func(solution, solution_idx):
    sum_weight = numpy.sum(solution * weights)
    sum_value = numpy.sum(solution * values)
    if sum_weight > backpack_limit:
        return 0
    else:
        return sum_value

fitness_function = fitness_func


sol_per_pop = 11
num_genes = len(items)
num_parents_mating = 5
num_generations = 30
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 11

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Параметры наилучшего решения: {solution}".format(solution=solution))
print("Фитнес-ценность лучшего решения = {solution_fitness}".format(solution_fitness=solution_fitness))

prediction = numpy.sum(solution * values)
print("Прогнозируемая стоимость товаров: {prediction}".format(prediction=prediction))

print("Предметы:", end=" ")
for i in range(len(items)):
    if solution[i] == 1:
        print("{item} ({weight})".format(item=items[i], weight=weights[i]), end=" ")

ga_instance.plot_fitness()
