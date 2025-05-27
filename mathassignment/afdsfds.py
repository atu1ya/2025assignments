import numpy as np
import matplotlib.pyplot as plt

# Parameters
f_max = 1
f_min = 0.05

# Frequency range
f = np.linspace(-1.2 * f_max, 1.2 * f_max, 1000)

# Spectral density function S_X(f)
S_X = np.piecewise(f,
                   [np.abs(f) < f_min, (np.abs(f) >= f_min) & (np.abs(f) <= f_max), np.abs(f) > f_max],
                   [0,
                    lambda f: (1 / f_max) * (f_max - np.abs(f)),
                    0])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(f, S_X, label=r'$S_X(f) = \frac{1}{f_{\max}}(f_{\max} - |f|)$', color='blue')

# Vertical dashed lines at ±f_min and ±f_max
for val, label in [(-f_max, r'$-f_{\max}$'), (-f_min, r'$-f_{\min}$'),
                   (f_min, r'$f_{\min}$'), (f_max, r'$f_{\max}$')]:
    plt.axvline(val, color='grey', linestyle='--')
    plt.text(val, 0.02, label, ha='center', va='bottom', fontsize=10)

# Highlight peak value
peak_value = (1 / f_max) * (f_max - f_min)
plt.plot(0, peak_value, 'ro')  # red dot at the peak
plt.text(0, peak_value + 0.02, rf'Max: ${peak_value:.2f}$', ha='center', fontsize=10)

# Highlight min value
plt.plot([f_min, -f_min], [0, 0], 'ro')  # red dots at min values
plt.text(f_min, -0.02, f'Min: 0', ha='center', fontsize=10)
plt.text(-f_min, -0.02, f'Min: 0', ha='center', fontsize=10)

# Labels and title
plt.title("Spectral Density $S_X(f)$ of Ocean Surface Displacement")
plt.xlabel("Frequency $f$")
plt.ylabel(r"$S_X(f)$")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
