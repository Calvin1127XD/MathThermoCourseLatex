"""
Draft visualization for phase diagram with wavy boundary.
The boundary is a sinusoidal-like curve going from left to right,
separating Phase 1 (top, phi=1) from Phase 2 (bottom, phi=-1).
The curve has an S-shape / snake shape going roughly from bottom-left to top-right area.
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# Box dimensions
box_w, box_h = 8, 6

# Draw outer box
rect = plt.Rectangle((0, 0), box_w, box_h, linewidth=3, edgecolor='black', facecolor='white')
ax.add_patch(rect)

# The wavy boundary curve
# Looking at the image: the curve starts from the left edge near the bottom,
# goes up in an S-shape, then continues to the right edge near the middle-top
# It's like a sinusoidal wave superimposed on a slightly rising line

x = np.linspace(0, box_w, 300)

# The curve appears to go:
# - starts at left edge around y=1.5 (low)
# - rises up to about y=4.5 (high) around x=3
# - dips back down to about y=2 around x=5
# - rises to about y=4.5 around x=6.5 (with a bump/hump)
# - levels off around y=3.5 near the right edge

# Let me try a combination: a baseline that rises slightly + sinusoidal wave
# Base: slight upward slope
base = 1.5 + 0.25 * x

# Sinusoidal wave with varying amplitude
# Main S-curve wave
wave = 1.2 * np.sin(0.9 * x - 0.5)

# Additional bump near right side
bump = 0.6 * np.exp(-((x - 6.5)**2) / 0.5)

y_boundary = base + wave + bump

# Clip to box
y_boundary = np.clip(y_boundary, 0.2, box_h - 0.2)

# Draw the interface band (gray shaded)
epsilon = 0.5  # half-width of interface
ax.fill_between(x, y_boundary - epsilon, y_boundary + epsilon,
                color='gray', alpha=0.3, zorder=2)

# Draw the boundary curve itself
ax.plot(x, y_boundary, 'k-', linewidth=2.5, zorder=3)

# Labels
ax.text(1.2, 5, r'$\phi = 1$', fontsize=18, ha='center', va='center')
ax.text(6, 5, 'Phase 1', fontsize=18, ha='center', va='center')
ax.text(1.5, 0.8, r'$\phi = -1$', fontsize=18, ha='center', va='center')
ax.text(6, 0.8, 'Phase 2', fontsize=18, ha='center', va='center')

# Epsilon arrow (red, double-headed)
arrow_x = 3.2
arrow_y_bottom = y_boundary[int(3.2/box_w * 300)] - epsilon
arrow_y_top = y_boundary[int(3.2/box_w * 300)] + epsilon
ax.annotate('', xy=(arrow_x, arrow_y_top), xytext=(arrow_x, arrow_y_bottom),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax.text(arrow_x + 0.3, (arrow_y_top + arrow_y_bottom)/2, r'$\varepsilon$',
        fontsize=18, color='red', ha='left', va='center')

ax.set_xlim(-0.5, box_w + 0.5)
ax.set_ylim(-0.5, box_h + 0.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase1-opus/draft.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("Draft saved.")
print(f"Boundary y-range: {y_boundary.min():.2f} to {y_boundary.max():.2f}")
print(f"Boundary at x=0: {y_boundary[0]:.2f}")
print(f"Boundary at x=4: {y_boundary[150]:.2f}")
print(f"Boundary at x=8: {y_boundary[-1]:.2f}")
