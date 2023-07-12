# Basic-Genetic-Algorithm-Code-Example

The code starts by importing the random module, which is used for generating random numbers.

The target list (target_list) represents the desired solution. It contains a sequence of numbers that the genetic algorithm will try to evolve towards.

The population size (population_size) determines how many individuals (candidate solutions) will be present in each generation.

The gene size (gene_size) is equal to the length of the target list. Each individual in the population represents a possible solution and has a list of numbers
with the same length as the target list.

The maximum generation count (max_generation) determines how many generations the algorithm will go through before terminating.

The create_individual() function generates a random individual by sampling the target list without replacement. It returns a list representing an individual.

The create_population() function creates a population by repeatedly calling create_individual() and adding the generated individuals to the population list.

The fitness() function calculates the fitness score of an individual. It compares each element of the individual's list with the corresponding element in the target list
and increments the fitness score if they match. The fitness score represents the similarity between the individual and the target list.

The selection() function performs tournament selection. It randomly selects a group of individuals (candidates) from the population and chooses 
the one with the highest fitness score as the selected individual. This process is repeated to fill the selected list with individuals.

The crossover() function performs single-point crossover between two parents. It randomly selects a crossover point and combines the first part of the first parent
with the second part of the second parent to create a child.

The mutation() function introduces random mutations into an individual. It randomly selects a gene (element) in the individual's list and replaces it 
with a randomly chosen element from the target list.

The next_generation() function generates the next generation by applying selection, crossover, and mutation operations. It repeatedly selects two parents from the population,
performs crossover to create a child, and optionally applies mutation to the child. This process continues until the new generation is filled with individuals.

The genetic_algorithm() function is the main driver function that orchestrates the genetic algorithm. It initializes the population, then iterates through generations.
In each generation, it performs selection, identifies the best individual with the highest fitness score, and prints the generation number, best individual,
and its fitness score. If an individual with a perfect fitness score (equal to the gene size) is found, the algorithm terminates. Otherwise, it proceeds to create the
next generation. Once the maximum generation count is reached, the algorithm terminates.

The genetic_algorithm() function is called at the end of the code to execute the genetic algorithm.

