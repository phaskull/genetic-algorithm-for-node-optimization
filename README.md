## Genetic Algorithm for Node Optimization

## Overview
This project implements a **Genetic Algorithm (GA)** to solve a **node optimization** problem in computational networks. The algorithm optimally configures or places nodes in a network to enhance performance, such as improving network coverage or resource utilization. 

### Features
- **Configurable Network Simulation**:
  - Adjustable number of nodes, constraints, and optimization parameters.
  - Ensures diversity in the initial population to enhance solution discovery.

- **Genetic Algorithm Implementation**:
  - Uses selection, crossover, and mutation to evolve solutions.
  - Supports both binary and real-valued chromosome representations.
  
- **Optimization & Evaluation**:
  - Evaluates node placement effectiveness based on fitness functions.
  - Compares GA results with alternative optimization methods.

---

## Project Structure
```
.
│── main.py                  # Main script to run the optimization
│── README.md                # Project documentation
│
├───src
│   │── ga.py                # Genetic Algorithm implementation
│   │── utils.py             # Helper functions
│   └── config.yaml          # Configuration settings
│
├───data
│   │── input.json           # Example input data
│   └── output.json          # Results of the GA optimization
│
├───results
│   ├── optimization_result.png  # Visualization of optimized node placements
│   ├── fitness_graph.png        # Convergence plot of GA generations
│   └── logs/                    # Logs of experiment runs
│
---

### 2. Running the Genetic Algorithm
Navigate to the project directory and execute:
```bash
python main.py
```
This will:
- Initialize a node optimization problem.
- Run the Genetic Algorithm.
- Generate **fitness reports** and **visualizations** of optimized node placements.

---

## Customizing the Genetic Algorithm

### Implementing a Custom Fitness Function
Modify `ga.py` to define a new fitness function:
```python
def custom_fitness_function(solution):
    # Compute fitness based on custom criteria
    return fitness_value
```
Then, update `main.py` to use your function:
```python
from src.ga import custom_fitness_function
GA = GeneticAlgorithm(fitness_function=custom_fitness_function)
```

### Adjusting GA Parameters
Modify **config.yaml** to fine-tune:
```yaml
population_size: 100
mutation_rate: 0.05
crossover_rate: 0.8
generations: 500
```

---

## Output Files
Results are saved in the **results/** directory:
- `optimization_result.png`: Shows the optimized node positions.
- `fitness_graph.png`: Displays the fitness improvement over generations.
- `output.json`: Stores the final optimized configuration.

---

## Example Workflow
1. **Run the optimization**:
   ```bash
   python main.py
   ```
2. **Analyze the results**:
   - Open `results/optimization_result.png` to visualize node placements.
   - Review `results/fitness_graph.png` for GA performance trends.

---

## Notes for Researchers & Developers
- **Modify only the fitness function or GA parameters** for customization.
- **Ensure correct handling of constraints** to avoid invalid solutions.
- **Test different crossover/mutation rates** for improved convergence.
- **Use logging and visualization** to debug and analyze optimization performance.

---

## License
This project is licensed under the **MIT License**. See `LICENSE` for details.

---

