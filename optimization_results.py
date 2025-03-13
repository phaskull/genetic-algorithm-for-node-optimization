import random
import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_parquet('job_table.parquet', engine='fastparquet')

# Select relevant columns
df = df[['req_nodes', 'num_cores_alloc', 'num_gpus_alloc', 'mem_alloc']].dropna()

# Ensure req_nodes is in string format
df['req_nodes'] = df['req_nodes'].astype(str)
df = df.explode('req_nodes')

# Convert memory from MB to GB
df['mem_alloc'] = df['mem_alloc'] / 1024  # Convert MB to GB

# Get the two nodes
node_usage = df.groupby('req_nodes').sum()
nodes = node_usage.index.tolist()

# Identify weakest and strongest node
strongest_node = node_usage.idxmax().unique()[0]
weakest_node = node_usage.idxmin().unique()[0]

# Maximum resources available in the strongest node
max_cores = node_usage.loc[strongest_node, 'num_cores_alloc']
max_gpus = node_usage.loc[strongest_node, 'num_gpus_alloc']
max_mem = node_usage.loc[strongest_node, 'mem_alloc']  # Now in GB

# Jobs assigned to the weakest node
weak_node_jobs = df[df['req_nodes'] == weakest_node]

# Define Genetic Algorithm parameters
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

# Fitness function - Determines if jobs can fit into the strongest node
def fitness(individual):
    total_cores = sum(individual[i] * weak_node_jobs.iloc[i]['num_cores_alloc'] for i in range(len(individual)))
    total_gpus = sum(individual[i] * weak_node_jobs.iloc[i]['num_gpus_alloc'] for i in range(len(individual)))
    total_mem = sum(individual[i] * weak_node_jobs.iloc[i]['mem_alloc'] for i in range(len(individual)))  # Now in GB
    

 # **If even a single job exceeds 256 GB, this solution is invalid!**
    if any(weak_node_jobs.iloc[i]['mem_alloc'] > 256 for i in range(len(individual)) if individual[i] == 1):       
        return 0  # Jobs that are too large to fit alone cannot be moved

    # If all jobs fit into strongest node, return a high fitness score
    if total_cores <= max_cores and total_gpus <= max_gpus and total_mem <= max_mem:
        return total_cores + total_gpus + total_mem  # Maximize resource utilization
    else:
        return 0  # Invalid solution


# Generate initial population (binary representation: 1 = move job, 0 = keep job in weak node)
population = [np.random.randint(2, size=len(weak_node_jobs)) for _ in range(POPULATION_SIZE)]

# Evolution loop
for generation in range(GENERATIONS):
    # Calculate fitness for each individual
    fitness_scores = [fitness(ind) for ind in population]

    # Select top individuals
    sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
    population = sorted_population[:POPULATION_SIZE//2]  # Keep the best half

    # Crossover - Combine top individuals
    for _ in range(POPULATION_SIZE//2):
        parent1, parent2 = random.choices(population, k=2)
        crossover_point = random.randint(0, len(weak_node_jobs) - 1)
        child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        population.append(child)

    # Mutation - Randomly flip a bit
    for individual in population:
        if random.random() < MUTATION_RATE:
            mutate_index = random.randint(0, len(weak_node_jobs) - 1)
            individual[mutate_index] = 1 - individual[mutate_index]  # Flip 0 to 1 or 1 to 0

# Select the best solution
best_solution = max(population, key=fitness)

# Apply job movement based on the best solution
for i, move in enumerate(best_solution):
    if move == 1:
        df.loc[df.index == weak_node_jobs.index[i], 'req_nodes'] = strongest_node

# Check if weakest node is now empty
if df[df['req_nodes'] == weakest_node].empty:
    print(f"Weakest node {weakest_node} is now empty and can be shut down.")
    df = df[df['req_nodes'] != weakest_node]  # Remove the weak node from the dataset

# Display final allocation
print(df[['req_nodes', 'num_cores_alloc', 'num_gpus_alloc', 'mem_alloc']])
