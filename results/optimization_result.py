import numpy as np
import matplotlib.pyplot as plt

# Sample Data (Replace with actual data)
nodes = np.arange(100)  # Replace with actual node indices
before_ga_cpu = np.random.randint(1000, 20000, size=100)  
after_ga_cpu = np.random.randint(1000, 20000, size=100)  

before_ga_gpu = np.random.randint(50, 700, size=100)  
after_ga_gpu = np.random.randint(50, 700, size=100)  
before_ga_mem = np.random.uniform(1, 40, size=100)  
after_ga_mem = np.random.uniform(1, 40, size=100)  

# Define bar width
width = 0.4  

# Create subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharex=True)

# CPU Allocation per Node
ax[0].bar(nodes - width/2, before_ga_cpu, width=width, label='Before GA', color='blue')
ax[0].bar(nodes + width/2, after_ga_cpu, width=width, alpha=0.6, label='After GA', color='orange')
ax[0].set_title("CPU Allocation per Node")
ax[0].set_xlabel("Nodes")
ax[0].set_ylabel("Total CPU Cores Allocated")
ax[0].legend()

# GPU Allocation per Node
ax[1].bar(nodes - width/2, before_ga_gpu, width=width, label='Before GA', color='blue')
ax[1].bar(nodes + width/2, after_ga_gpu, width=width, alpha=0.6, label='After GA', color='orange')
ax[1].set_title("GPU Allocation per Node")
ax[1].set_xlabel("Nodes")
ax[1].set_ylabel("Total GPUs Allocated")
ax[1].legend()

# Memory Allocation per Node
ax[2].bar(nodes - width/2, before_ga_mem, width=width, label='Before GA', color='blue')
ax[2].bar(nodes + width/2, after_ga_mem, width=width, alpha=0.6, label='After GA', color='orange')
ax[2].set_title("Memory Allocation per Node (GB)")
ax[2].set_xlabel("Nodes")
ax[2].set_ylabel("Total Memory Allocated (GB)")
ax[2].legend()

# Show the plot
plt.tight_layout()
plt.show()
