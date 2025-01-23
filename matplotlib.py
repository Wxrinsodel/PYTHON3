import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)  # Generate x values from -10 to 10
f_x = x**2                     # Calculate f(x) = x^2 for each x

# Step 2: Plot the graph of f(x)
plt.plot(x, f_x, label='f(x) = x^2', color='blue')

# Step 3: Add plot labels and legend
plt.title('Graph of f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Step 4: Display the graph
plt.grid()
plt.show()
