import numpy as np
import matplotlib.pyplot as plt

def h_n(x, n):
    """Auxiliary function h_n defined in [0, 1] (mostly)"""
    # Vectorized conditional logic
    val = np.zeros_like(x)
    
    # Conditions
    cond1 = (x >= 0) & (x <= 2**(-n))
    cond2 = (x > 2**(-n)) & (x <= 2**(1-n))
    
    # Apply formulas
    val[cond1] = (2**n) * x[cond1]
    val[cond2] = 2 - (2**n) * x[cond2]
    
    return val

def f(x_array):
    """Main function f(x) defined piece-wise on [n, n+1]"""
    y_array = np.zeros_like(x_array)
    
    # Determine which n corresponds to each x
    # Since n = 1, 2, ... we iterate through relevant n
    # We only care about positive x for this problem context
    
    # Let's handle x element-wise or by masking for efficiency
    # Max x in plot
    max_x = np.ceil(np.max(x_array))
    
    for n in range(1, int(max_x) + 1):
        # The interval for a specific n is [n, n+1]
        mask = (x_array >= n) & (x_array < n + 1)
        if np.any(mask):
            # for x in [n, n+1], f(x) = h_n(x - n)
            x_shifted = x_array[mask] - n
            y_array[mask] = h_n(x_shifted, n)
            
    return y_array

# Setup plot
x = np.linspace(0, 5, 5000) # Plot for n=1 to 4 roughly
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x)')
plt.title(r'Visualization of Counterexample Function $f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)

# Add some text annotations to explain the peaks
for n in range(1, 5):
    peak_x = n + 2**(-n)
    plt.annotate(f'n={n}\nPeak at x={peak_x:.4f}', 
                 xy=(peak_x, 1), 
                 xytext=(peak_x, 1.1),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='center')

plt.ylim(-0.1, 1.3)
# Save the figure instead of showing it, as it's more reliable in this environment
output_path = 'counterexample_visualization.png'
plt.savefig(output_path)
print(f"Plot saved to {output_path}")
