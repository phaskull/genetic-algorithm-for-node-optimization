import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self, config):
        self.population_size = config['population_size']
        self.mutation_rate = config['mutation_rate']
        self.generations = config['generations']

    def fitness(self, solution):
        return np.sum(solution)  # Basit fitness fonksiyonu

    def mutate(self, solution):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, len(solution) - 1)
            solution[idx] = 1 - solution[idx]
        return solution

    def run(self):
        population = [np.random.randint(2, size=10) for _ in range(self.population_size)]
        for _ in range(self.generations):
            population = sorted(population, key=self.fitness, reverse=True)
            best_solution = population[0]
            if self.fitness(best_solution) > 9:
                return best_solution
            new_population = [self.mutate(best_solution.copy()) for _ in range(self.population_size)]
            population = new_population
        return best_solution
