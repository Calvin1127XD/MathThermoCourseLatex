import matplotlib.pyplot as plt
import numpy as np

# Phase diagram: Temperature vs x_1 (mole fraction)
# Both curves are symmetric parabolas centered at x = 0.5

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

x = np.linspace(0, 1, 200)
x_c = 0.5  # critical point (center of symmetry)

# Binodal curve (outer, wider)
# Appears to touch x-axis around x=0.05 and x=0.95 (width ~ 0.9)
# Peak at around T ~ 0.9 (relative to axis height)

# Spinodal curve (inner, narrower)
# Appears to touch x-axis around x=0.2 and x=0.8 (width ~ 0.6)
# Same peak height as binodal (they meet at critical point)

# Candidate 1: Simple quadratic parabolas
T_c1 = 0.9  # Critical temperature (peak)
binodal_width1 = 0.45  # half-width for binodal
spinodal_width1 = 0.30  # half-width for spinodal

# y = T_c * (1 - ((x - 0.5)/width)^2) but only positive part
binodal1 = T_c1 * (1 - ((x - x_c)/binodal_width1)**2)
binodal1 = np.maximum(binodal1, 0)

spinodal1 = T_c1 * (1 - ((x - x_c)/spinodal_width1)**2)
spinodal1 = np.maximum(spinodal1, 0)

axes[0].plot(x, binodal1, 'k-', linewidth=2, label='Binodal')
axes[0].plot(x, spinodal1, 'k--', linewidth=2, label='Spinodal')
axes[0].plot(0.5, T_c1, 'rx', markersize=12, markeredgewidth=3)
axes[0].set_xlabel('$x_1$')
axes[0].set_ylabel('Temperature')
axes[0].set_title('Candidate 1: Simple quadratic\nbinodal_w=0.45, spinodal_w=0.30')
axes[0].legend()
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 1)

# Candidate 2: Adjusted widths - binodal narrower at base
T_c2 = 0.9
binodal_width2 = 0.42
spinodal_width2 = 0.28

binodal2 = T_c2 * (1 - ((x - x_c)/binodal_width2)**2)
binodal2 = np.maximum(binodal2, 0)

spinodal2 = T_c2 * (1 - ((x - x_c)/spinodal_width2)**2)
spinodal2 = np.maximum(spinodal2, 0)

axes[1].plot(x, binodal2, 'k-', linewidth=2, label='Binodal')
axes[1].plot(x, spinodal2, 'k--', linewidth=2, label='Spinodal')
axes[1].plot(0.5, T_c2, 'rx', markersize=12, markeredgewidth=3)
axes[1].set_xlabel('$x_1$')
axes[1].set_ylabel('Temperature')
axes[1].set_title('Candidate 2: quadratic\nbinodal_w=0.42, spinodal_w=0.28')
axes[1].legend()
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)

# Candidate 3: Based on original image - binodal reaches ~0.08 to ~0.92
# spinodal reaches ~0.22 to ~0.78
T_c3 = 0.85  # slightly lower peak
binodal_width3 = 0.43  # zeros at 0.07 and 0.93
spinodal_width3 = 0.28  # zeros at 0.22 and 0.78

binodal3 = T_c3 * (1 - ((x - x_c)/binodal_width3)**2)
binodal3 = np.maximum(binodal3, 0)

spinodal3 = T_c3 * (1 - ((x - x_c)/spinodal_width3)**2)
spinodal3 = np.maximum(spinodal3, 0)

axes[2].plot(x, binodal3, 'k-', linewidth=2, label='Binodal')
axes[2].plot(x, spinodal3, 'k--', linewidth=2, label='Spinodal')
axes[2].plot(0.5, T_c3, 'rx', markersize=12, markeredgewidth=3)
axes[2].set_xlabel('$x_1$')
axes[2].set_ylabel('Temperature')
axes[2].set_title('Candidate 3: quadratic\nbinodal_w=0.43, spinodal_w=0.28, T_c=0.85')
axes[2].legend()
axes[2].set_xlim(0, 1)
axes[2].set_ylim(0, 1)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase2-phase-diagram/candidates.png', dpi=150)
plt.close()

print("Saved candidates.png")
print("\nAnalysis:")
print("- All candidates use downward-opening parabolas (quadratic)")
print("- The curves appear symmetric about x=0.5")
print("- Key parameters: T_c (peak height), width (half-width of parabola)")
print("- Binodal is wider (outer curve)")
print("- Spinodal is narrower (inner curve)")
