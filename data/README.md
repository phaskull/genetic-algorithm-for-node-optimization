# Job Optimization Data - PM100 Dataset Integration

## Overview
This repository contains job optimization data based on the **PM100 Dataset**. The dataset is integrated with a **Genetic Algorithm-based optimization approach**, focusing on workload redistribution across nodes to enhance computational efficiency.

## Data Structure
The dataset consists of two primary JSON files:

### **1 `input.json` (Job Allocation Data)**
This file contains information about jobs, their assigned nodes, and resource allocations.

### **2 `output.json` (Optimized Job Distribution)**
This file contains the results of the optimization, indicating which jobs were migrated and which nodes can be shut down.

## PM100 Dataset Integration
The job allocation data in `input.json` is derived from the **[PM100 Dataset](https://github.com/francescoantici/PM100-data)**, which provides real-world job scheduling information from HPC systems. The dataset has been processed to:

- Extract **job execution details** such as core allocation, GPU usage, and memory requirements.
- Identify **underperforming nodes** for optimization.
- Simulate **job redistribution** across more efficient nodes using a Genetic Algorithm.

## How to Use This Data
1. **Load `input.json`** into your optimization system.
2. **Apply optimization logic** (e.g., Genetic Algorithm, heuristic-based job scheduling).
3. **Compare results** by analyzing `output.json` to see improvements in resource allocation.
4. **Further enhance the optimization** by testing with different GA parameters or heuristics.

## Future Improvements
- Expanding job allocation data by integrating additional PM100 dataset features.
- Implementing multi-objective optimization for balancing CPU, GPU, and memory efficiency.
- Automating the conversion of PM100 raw logs into structured JSON for easy integration.

## Acknowledgments
This project leverages the **PM100 Dataset** ([GitHub Repo](https://github.com/francescoantici/PM100-data)) to create a real-world optimization scenario. All rights and acknowledgments belong to the dataset authors.

---
