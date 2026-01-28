import matplotlib.pyplot as plt
import numpy as np

# Create the wavy boundary
# The boundary should have multiple waves across the width
x = np.linspace(0, 10, 200)

# Experiment with sine wave parameters
# y = A * sin(B*x + C) + D
# A = amplitude (vertical oscillation)
# B = frequency (number of waves)
# C = phase shift
# D = vertical offset (middle of box)

A = 0.4  # amplitude
B = 2 * np.pi / 2.5  # frequency (about 4 waves in 10 units)
C = 0  # no phase shift
D = 5.0  # center of box vertically

y = A * np.sin(B * x + C) + D

# Create the gray shaded region (interface width epsilon)
epsilon = 0.5  # interface width
y_upper = y + epsilon/2
y_lower = y - epsilon/2

# Plot
fig, ax = plt.subplots(figsize=(8, 5))

# Draw box
ax.plot([0, 10, 10, 0, 0], [0, 0, 10, 10, 0], 'k-', linewidth=2)

# Draw wavy boundary
ax.plot(x, y, 'k-', linewidth=2)

# Draw gray shaded region
ax.fill_between(x, y_lower, y_upper, color='gray', alpha=0.5)

# Add labels
ax.text(5, 7.5, r'$\phi = 1$', fontsize=14, ha='left')
ax.text(8, 7.5, 'Phase 1', fontsize=14, ha='center')
ax.text(0.5, 2.5, r'$\phi = -1$', fontsize=14, ha='left')
ax.text(8, 2.5, 'Phase 2', fontsize=14, ha='center')

# Add epsilon arrow (approximate location)
arrow_x = 2.5
arrow_y = y[int(len(y) * arrow_x / 10)]
ax.annotate('', xy=(arrow_x, arrow_y + epsilon/2), xytext=(arrow_x, arrow_y - epsilon/2),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax.text(arrow_x + 0.3, arrow_y, r'$\varepsilon$', fontsize=14, color='red')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase1-sonnet/draft.png', dpi=150, bbox_inches='tight')
print("Draft saved to draft.png")
print(f"Parameters: A={A}, B={B:.3f}, C={C}, D={D}, epsilon={epsilon}")
