import numpy as np
import matplotlib.pyplot as plt

# Create a generic plot with clear labels
plt.figure(figsize=(10, 6))

# Define generic frequency range
f = np.linspace(-1.5, 1.5, 1000)

# Define generic parameters (unitless)
f_min = 0.5
f_max = 1.0

# Calculate the spectral density
S_X = np.zeros_like(f)
for i, freq in enumerate(f):
    if f_min <= abs(freq) <= f_max:
        S_X[i] = (1/f_max) * (f_max - abs(freq))

# Plot the spectral density function
plt.plot(f, S_X, 'b-', linewidth=2.5)
plt.fill_between(f, S_X, alpha=0.2, color='blue')

# Add labels and title
plt.xlabel('Frequency (f)', fontsize=14)
plt.ylabel('Spectral Density $S_X(f)$', fontsize=14)
plt.title('Truncated Triangular Spectral Density Function', fontsize=16)

# Add labels for key frequencies
plt.annotate('$-f_{max}$', xy=(-f_max, 0), xytext=(-f_max, -0.1), 
             ha='center', fontsize=12)
plt.annotate('$-f_{min}$', xy=(-f_min, (1/f_max)*(f_max-f_min)), 
             xytext=(-f_min, (1/f_max)*(f_max-f_min)+0.1), 
             ha='center', fontsize=12)
plt.annotate('$f_{min}$', xy=(f_min, (1/f_max)*(f_max-f_min)), 
             xytext=(f_min, (1/f_max)*(f_max-f_min)+0.1), 
             ha='center', fontsize=12)
plt.annotate('$f_{max}$', xy=(f_max, 0), xytext=(f_max, -0.1), 
             ha='center', fontsize=12)

# Add formula text (split into parts to avoid LaTeX cases environment)
plt.text(0, 0.8, "$S_X(f) = \\frac{1}{f_{max}}(f_{max} - |f|)$ for $f_{min} ≤ |f| ≤ f_{max}$", 
         ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))
plt.text(0, 0.65, "$S_X(f) = 0$ otherwise", 
         ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# Add peak height label
plt.annotate('$\\frac{1}{f_{max}}(f_{max}-f_{min})$', 
             xy=(f_min, (1/f_max)*(f_max-f_min)), 
             xytext=(f_min+0.2, (1/f_max)*(f_max-f_min)), 
             ha='left', fontsize=12, 
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

# Improve appearance
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Set y-axis limits to show a bit of space below 0
plt.ylim(-0.15, 1.2)

# Don't use tight_layout() which was causing the error
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()