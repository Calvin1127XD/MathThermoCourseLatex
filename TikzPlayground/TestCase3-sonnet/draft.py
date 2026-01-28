import matplotlib.pyplot as plt
import numpy as np

# Define the domain
x = np.linspace(-1, 4, 300)

# Define x=a, x=b, x=c positions (estimated from image)
a = 0.5
b = 2.0
c = 3.0

# Analyze curve properties:
# f(x) (blue): starts low, curves up (concave up), increasing
# - Could be exponential-like or quadratic
# - Let's try: f(x) = 0.3*(x-1)^2 + 1 or similar

# h(x) (red): starts high, curves down (concave down), decreasing
# - Could be negative quadratic or inverse exponential
# - Let's try: h(x) = -0.3*(x-1)^2 + 4

# g(x) (green): parabola with minimum around x=b
# - Clear parabola shape
# - Let's try: g(x) = 0.5*(x-2)^2 + 0.5

# Test different parameter combinations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Version 1: Basic quadratics
ax = axes[0, 0]
f1 = 0.3*(x-1)**2 + 1
h1 = -0.3*(x-1)**2 + 4
g1 = 0.5*(x-2)**2 + 0.5

ax.plot(x, f1, 'b-', linewidth=2, label='f(x)')
ax.plot(x, h1, 'r-', linewidth=2, label='h(x)')
ax.plot(x, g1, 'g-', linewidth=2, label='g(x)')
ax.axvline(a, color='gray', linestyle='--', alpha=0.5)
ax.axvline(b, color='gray', linestyle='--', alpha=0.5)
ax.axvline(c, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Version 1: Basic quadratics')
ax.set_xlim(-0.5, 4)
ax.set_ylim(-1, 5)

# Version 2: Adjusted curves
ax = axes[0, 1]
f2 = 0.25*(x-0.5)**2 + 0.8
h2 = -0.25*(x-0.5)**2 + 3.8
g2 = 0.4*(x-2)**2 + 0.3

ax.plot(x, f2, 'b-', linewidth=2, label='f(x)')
ax.plot(x, h2, 'r-', linewidth=2, label='h(x)')
ax.plot(x, g2, 'g-', linewidth=2, label='g(x)')
ax.axvline(a, color='gray', linestyle='--', alpha=0.5)
ax.axvline(b, color='gray', linestyle='--', alpha=0.5)
ax.axvline(c, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Version 2: Adjusted parameters')
ax.set_xlim(-0.5, 4)
ax.set_ylim(-1, 5)

# Version 3: Using exponential for f, inverse exp for h
ax = axes[1, 0]
f3 = 0.5*np.exp(0.4*x) + 0.3
h3 = 4 - 0.5*np.exp(0.4*x)
g3 = 0.4*(x-2)**2 + 0.3

ax.plot(x, f3, 'b-', linewidth=2, label='f(x)')
ax.plot(x, h3, 'r-', linewidth=2, label='h(x)')
ax.plot(x, g3, 'g-', linewidth=2, label='g(x)')
ax.axvline(a, color='gray', linestyle='--', alpha=0.5)
ax.axvline(b, color='gray', linestyle='--', alpha=0.5)
ax.axvline(c, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Version 3: Exponential curves')
ax.set_xlim(-0.5, 4)
ax.set_ylim(-1, 5)

# Version 4: Cubic for smoother transitions
ax = axes[1, 1]
f4 = 0.05*x**3 + 0.1*x**2 + 0.2*x + 1
h4 = -0.05*x**3 - 0.1*x**2 + 0.2*x + 3.5
g4 = 0.35*(x-2)**2 + 0.4

ax.plot(x, f4, 'b-', linewidth=2, label='f(x)')
ax.plot(x, h4, 'r-', linewidth=2, label='h(x)')
ax.plot(x, g4, 'g-', linewidth=2, label='g(x)')
ax.axvline(a, color='gray', linestyle='--', alpha=0.5)
ax.axvline(b, color='gray', linestyle='--', alpha=0.5)
ax.axvline(c, color='gray', linestyle='--', alpha=0.5)
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_title('Version 4: Cubic curves')
ax.set_xlim(-0.5, 4)
ax.set_ylim(-1, 5)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase3-sonnet/draft.png', dpi=150)
print("Draft saved!")

# Let's also create a final version that best matches
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Based on the image, the curves seem to be smooth quadratics
# with the shaded area between them
f_final = 0.25*x**2 + 0.5*x + 0.5
h_final = -0.25*x**2 + 0.5*x + 3.5
g_final = 0.35*(x-2)**2 + 0.4

# Plot curves
ax2.plot(x, f_final, 'b-', linewidth=2.5, label='f(x)')
ax2.plot(x, h_final, 'r-', linewidth=2.5, label='h(x)')
ax2.plot(x, g_final, 'g-', linewidth=2.5, label='g(x)')

# Vertical lines
ax2.axvline(a, color='gray', linewidth=1.5, linestyle='-')
ax2.axvline(b, color='gray', linewidth=1.5, linestyle='-')
ax2.axvline(c, color='gray', linewidth=1.5, linestyle='-')

# Add labels for vertical lines
ax2.text(a, -0.8, 'x=a', ha='center', fontsize=12)
ax2.text(b, -0.8, 'x=b', ha='center', fontsize=12)
ax2.text(c, -0.8, 'x=c', ha='center', fontsize=12)

# Shading - need to determine which curves bound the region
# From image: shaded between f(x) from below and h(x) from above for x in [a,b]
# and between g(x) from below and h(x) from above for x in [b,c]
x_shade1 = np.linspace(a, b, 100)
f_shade1 = 0.25*x_shade1**2 + 0.5*x_shade1 + 0.5
h_shade1 = -0.25*x_shade1**2 + 0.5*x_shade1 + 3.5
ax2.fill_between(x_shade1, f_shade1, h_shade1, color='gray', alpha=0.3)

x_shade2 = np.linspace(b, c, 100)
g_shade2 = 0.35*(x_shade2-2)**2 + 0.4
h_shade2 = -0.25*x_shade2**2 + 0.5*x_shade2 + 3.5
ax2.fill_between(x_shade2, g_shade2, h_shade2, color='gray', alpha=0.3)

# Axes
ax2.axhline(0, color='black', linewidth=1.5)
ax2.axvline(0, color='black', linewidth=1.5)
ax2.arrow(3.8, 0, 0.15, 0, head_width=0.2, head_length=0.08, fc='black', ec='black')
ax2.arrow(0, 4.8, 0, 0.15, head_width=0.15, head_length=0.08, fc='black', ec='black')

ax2.set_xlim(-0.5, 4.2)
ax2.set_ylim(-1, 5.2)
ax2.set_xlabel('x', fontsize=14)
ax2.grid(True, alpha=0.2)
ax2.legend(fontsize=12)
ax2.set_title('Final version for TikZ', fontsize=14)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase3-sonnet/draft_final.png', dpi=150)
print("Final draft saved!")
print("\nFinal parameters:")
print(f"f(x) = 0.25*x^2 + 0.5*x + 0.5")
print(f"h(x) = -0.25*x^2 + 0.5*x + 3.5")
print(f"g(x) = 0.35*(x-2)^2 + 0.4")
print(f"a = {a}, b = {b}, c = {c}")
