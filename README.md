# Genetic Algorithm for Finding the Optimal Sequence

This Python program implements a genetic algorithm to find the optimal sequence that matches a target list. The algorithm evolves a population of individuals, each represented by a sequence of numbers, towards the target list.

## How it Works

The genetic algorithm follows these steps:

1.  **Initialization**: The target list is defined, along with parameters such as population size, gene size, and maximum generation count.
    
2.  **Population Creation**: A random population is created, with each individual consisting of a sequence of numbers randomly selected from the target list.
    
3.  **Fitness Evaluation**: The fitness score of each individual is calculated by comparing its sequence of numbers with the target list. The fitness score represents the similarity between an individual and the target list.
    
4.  **Selection**: Tournament selection is performed to select individuals for the next generation. A group of individuals (candidates) is randomly selected from the population, and the one with the highest fitness score is chosen as a selected individual. This process is repeated to fill the next generation.
    
5.  **Crossover**: Single-point crossover is applied to pairs of selected individuals. A random crossover point is selected, and the subsequences before and after the crossover point are swapped between the parents to create a child individual.
    
6.  **Mutation**: Random mutations are introduced to maintain diversity in the population. A gene (number) in an individual's sequence is randomly selected and replaced with a randomly chosen number from the target list.
    
7.  **Next Generation**: The new generation is created by repeating the selection, crossover, and mutation steps until the population size is reached.
    
8.  **Termination**: The algorithm iterates through generations until it finds an individual with a perfect fitness score (equal to the gene size) or reaches the maximum generation count.
    

## Getting Started

To run the genetic algorithm, follow these steps:

1.  Install Python (version 3.6 or later) on your machine.
    
2.  Clone this repository or download the `genetic_algorithm.py` file.
    
3.  Open a terminal or command prompt and navigate to the directory containing the `genetic_algorithm.py` file.
    
4.  Run the following command to execute the program:
    
    shellCopy code
    
    `python genetic_algorithm.py` 
    
5.  The program will display each generation's best individual and its fitness score until it finds an optimal solution or reaches the maximum generation count.
    

## Customization

You can customize the genetic algorithm by adjusting the following parameters in the `genetic_algorithm.py` file:

-   `target_list`: The desired sequence that the algorithm will try to evolve towards.
-   `population_size`: The number of individuals in each generation.
-   `gene_size`: The length of the individual's sequence (should match the target list length).
-   `max_generation`: The maximum number of generations the algorithm will go through.

Feel free to modify these parameters and experiment with different target lists and configurations to observe how the algorithm performs.

## Requirements

-   Python 3.6 or later
