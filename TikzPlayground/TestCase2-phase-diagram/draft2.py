import matplotlib.pyplot as plt
import numpy as np

# Refined phase diagram based on original image analysis
# The binodal appears to touch x-axis around x=0.08 and x=0.92
# The spinodal appears to touch x-axis around x=0.22 and x=0.78

fig, ax = plt.subplots(figsize=(8, 6))

x = np.linspace(0, 1, 200)
x_c = 0.5  # critical point (center of symmetry)

# For a parabola y = a*(x - x1)*(x - x2) with peak at x_c = (x1+x2)/2
# The peak height is -a*(x_c - x1)*(x_c - x2) = -a * w^2 where w = half-width

# Binodal: zeros at x1=0.08, x2=0.92, so width = 0.42 each side
# Peak height should be around 0.85-0.9
x1_bin, x2_bin = 0.08, 0.92
T_c = 0.88  # critical temperature

# Calculate coefficient: T_c = -a * (0.5 - 0.08) * (0.5 - 0.92) = -a * 0.42 * (-0.42) = a * 0.1764
# So a = T_c / 0.1764 = 4.99
a_bin = T_c / ((x_c - x1_bin) * (x2_bin - x_c))

binodal = -a_bin * (x - x1_bin) * (x - x2_bin)
binodal = np.maximum(binodal, 0)

# Spinodal: zeros at x1=0.22, x2=0.78
x1_spin, x2_spin = 0.22, 0.78
a_spin = T_c / ((x_c - x1_spin) * (x2_spin - x_c))

spinodal = -a_spin * (x - x1_spin) * (x - x2_spin)
spinodal = np.maximum(spinodal, 0)

# Plot
ax.plot(x, binodal, 'k-', linewidth=2.5, label='Binodal')
ax.plot(x, spinodal, 'k--', linewidth=2.5, label='Spinodal')
ax.plot(0.5, T_c, 'rx', markersize=15, markeredgewidth=3)

# Add metastable zone annotation
# Arrow at around x=0.25, between the two curves
x_arrow = 0.25
y_bin_at_arrow = -a_bin * (x_arrow - x1_bin) * (x_arrow - x2_bin)
y_spin_at_arrow = max(0, -a_spin * (x_arrow - x1_spin) * (x_arrow - x2_spin))

ax.annotate('', xy=(x_arrow, y_spin_at_arrow + 0.02), xytext=(x_arrow, y_bin_at_arrow - 0.02),
            arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))

ax.text(0.15, 0.65, 'Metastable\nZone', fontsize=12, ha='center')
# Draw line from text to arrow region
ax.plot([0.18, 0.23], [0.55, 0.45], 'k-', linewidth=1)

ax.set_xlabel('$x_1$', fontsize=14)
ax.set_ylabel('Temperature', fontsize=14)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax.legend(loc='upper right', fontsize=12)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase2-phase-diagram/draft.png', dpi=150)
plt.close()

print("Saved draft.png")
print(f"\nFinal parameters:")
print(f"Binodal: zeros at x={x1_bin} and x={x2_bin}")
print(f"Spinodal: zeros at x={x1_spin} and x={x2_spin}")
print(f"Critical temperature T_c = {T_c}")
print(f"\nFor TikZ/pgfplots:")
print(f"Binodal: y = -{a_bin:.4f} * (x - {x1_bin}) * (x - {x2_bin})")
print(f"Spinodal: y = -{a_spin:.4f} * (x - {x1_spin}) * (x - {x2_spin})")
