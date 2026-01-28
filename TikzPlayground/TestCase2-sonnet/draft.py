import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# x-axis: composition from 0 to 1
x = np.linspace(0, 1, 200)

# Experiment with symmetric bell-shaped curves
# Using parabolas centered at x = 0.5

# Binodal curve (wider, outer curve)
# Appears to touch the x-axis at x ≈ 0.2 and x ≈ 0.8
# Maximum at x = 0.5
# Using: T = -a(x - 0.5)^2 + T_max_binodal
# At x = 0.2 or 0.8: T = 0
# 0 = -a(0.2 - 0.5)^2 + T_max
# 0 = -a(0.09) + T_max
# T_max = 0.09*a

# Let's say T_max_binodal = 1.0 (normalized)
# Then: 1.0 = 0.09*a → a = 1.0/0.09 ≈ 11.11

a_binodal = 1.0 / 0.09
T_binodal = -a_binodal * (x - 0.5)**2 + 1.0

# Spinodal curve (narrower, inner curve)
# Appears to touch the x-axis at x ≈ 0.3 and x ≈ 0.7
# Maximum at x = 0.5 (marked with red X)
# Same logic: 0 = -b(0.3 - 0.5)^2 + T_max_spinodal
# 0 = -b(0.04) + T_max
# If T_max_spinodal = 0.8 (slightly lower than binodal)
# Then: b = 0.8 / 0.04 = 20

T_max_spinodal = 0.8
b_spinodal = T_max_spinodal / 0.04
T_spinodal = -b_spinodal * (x - 0.5)**2 + T_max_spinodal

# Plot
ax.plot(x, T_binodal, 'k-', linewidth=2, label='Binodal')
ax.plot(x, T_spinodal, 'k--', linewidth=2, label='Spinodal')

# Mark the spinodal maximum with red X
ax.plot(0.5, T_max_spinodal, 'rx', markersize=15, markeredgewidth=3)

# Add metastable zone label and arrow
ax.text(0.15, 0.7, 'Metastable\nZone', fontsize=14, va='center')
ax.annotate('', xy=(0.3, 0.5), xytext=(0.35, 0.5),
            arrowprops=dict(arrowstyle='<->', lw=1.5))

# Set axis properties
ax.set_xlabel('$x_1$', fontsize=14)
ax.set_ylabel('Temperature', fontsize=14)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.1)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.grid(False)

# Legend
ax.legend(loc='upper right', fontsize=12, frameon=False)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase2-sonnet/draft.png', dpi=150)
print("Draft saved!")
print(f"Binodal: T = -{a_binodal:.2f}(x - 0.5)^2 + 1.0")
print(f"Spinodal: T = -{b_spinodal:.2f}(x - 0.5)^2 + {T_max_spinodal}")
