import random

# Target list
target_list = [4, 7, 2, 9, 5, 1, 8, 3, 6]

# Population size
population_size = 50

# Gene size (length of the list)
gene_size = len(target_list)

# Maximum generation count
max_generation = 50

def create_individual():
    # Create a random individual
    individual = random.sample(target_list, gene_size)
    return individual

def create_population():
    # Create a random population
    population = []
    for _ in range(population_size):
        individual = create_individual()
        population.append(individual)
    return population

def fitness(individual):
    # Calculate the fitness score of an individual
    fitness_score = 0
    for i in range(gene_size):
        if individual[i] == target_list[i]:
            fitness_score += 1
    return fitness_score

def selection(population):
    # Tournament selection
    selected = []
    for _ in range(population_size):
        candidates = random.sample(population, 5)
        selected.append(max(candidates, key=fitness))
    return selected

def crossover(parent1, parent2):
    # Single-point crossover
    crossover_point = random.randint(1, gene_size - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutation(individual):
    # Random mutation
    index = random.randint(0, gene_size - 1)
    individual[index] = random.choice(target_list)
    return individual

def next_generation(population):
    # Create the next generation
    new_generation = []
    while len(new_generation) < population_size:
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child = crossover(parent1, parent2)
        if random.random() < 0.1:  # Mutation rate: 10%
            child = mutation(child)
        new_generation.append(child)
    return new_generation

def genetic_algorithm():
    population = create_population()

    for generation in range(max_generation):
        population = selection(population)
        best_individual = max(population, key=fitness)
        # Print the best individual and its fitness score in each generation
        print(f"Generation: {generation + 1}\tBest Individual: {best_individual}\tFitness: {fitness(best_individual)}")

        if fitness(best_individual) == gene_size:
            print("Genetic Algorithm completed.")
            return

        population = next_generation(population)

    print("Maximum generation count reached. Genetic Algorithm completed.")

genetic_algorithm()