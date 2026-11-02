import numpy as np

# Quantity of farm inputs
Q = np.array([
    [10, 5, 2],
    [6, 8, 3]
])

# Price of each input in Kenya shillings
P = np.array([
    [3000],
    [500],
    [800]
])

# Calculate total cost using matrix multiplication
total_cost = Q @ P

print("Farm A total cost: KSh", total_cost[0, 0])
print("Farm B total cost: KSh", total_cost[1, 0])
