import numpy as np

generations = np.arange(1, GENERATIONS + 1)
best_fitness_values = np.random.randint(50, 200, size=GENERATIONS).cumsum() / np.arange(1, GENERATIONS + 1)  

plt.figure(figsize=(10, 5))
plt.plot(generations, best_fitness_values, marker='o', linestyle='-', color='blue', label='Best Fitness')
plt.xlabel("Generations")
plt.ylabel("Best Fitness Score")
plt.title("Fitness Evolution Over Generations")
plt.legend()
plt.grid()
plt.show()
