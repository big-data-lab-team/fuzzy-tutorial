from scipy.optimize import fsolve
import numpy as np

# Define the quadratic equation as a function
def quadratic_eq(x):
    return 7169 * x**2 - 8686 * x + 2631

results = []
for _ in range(1,11):
    # Use fsolve to find roots, providing initial guesses
    results.append( [ fsolve(quadratic_eq, 0), fsolve(quadratic_eq, 1) ])

np.save('/data/mca_quadratic_results.npy', np.array(results))
