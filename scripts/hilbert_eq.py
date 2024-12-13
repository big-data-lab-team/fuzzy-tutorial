import numpy as np
from scipy.linalg import inv

# Function to generate a Hilbert matrix of size n x n
def hilbert_matrix(n):
    return np.fromfunction(lambda i, j: 1.0 / (i + j + 1), (n, n))
# Define the size of the matrix
n = 5  # Example size (can change as needed)
# Generate the Hilbert matrix
H = hilbert_matrix(n)
results = []
for _ in range(1,11):
    # Calculate the inverse using scipy.linalg.inv
    H_inv = inv(H)
    results.append(H_inv)
np.save("/data/mca_hilbert_results.npy", np.array(results, dtype=np.float64))