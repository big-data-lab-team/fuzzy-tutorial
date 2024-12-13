#Sample implementation 

# Define the iterative formula
def iterative_formula(x_k):
    numerator = 3 * x_k**4 - 20 * x_k**3 + 35 * x_k**2 - 24
    denominator = 4 * x_k**3 - 30 * x_k**2 + 70 * x_k - 50
    return numerator / denominator

# Initialize variables
x_k = 1.5100050721319  # Initial guess
iterations = 30

# Perform iterations
results = [x_k]  # To store all iteration results
for _ in range(iterations):
    x_k = iterative_formula(x_k)
    results.append(x_k)


file_path = '/data/mca_convergence_results.txt'

# Open the file in append mode, which creates the file if it doesn't exist
with open(file_path, 'a') as file:
    file.write(f"{results[-1]}\n")  # Append the value after 30 iterations