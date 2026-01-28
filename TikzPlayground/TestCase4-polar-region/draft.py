"""
Python draft for TestCase4 - Polar coordinate region diagram

The diagram shows:
- Two rays from origin at angles alpha and beta
- Inner curve r = h1(theta) (red)
- Outer curve r = h2(theta) (blue)
- Shaded region between curves (green)

Key observations from the original image:
- alpha is roughly 20-30 degrees (lower ray)
- beta is roughly 60-70 degrees (upper ray)
- Both curves are smooth and convex outward
- h1 < h2 for all theta in [alpha, beta]
- The curves don't have specific equations - they're generic smooth curves
"""

import numpy as np
import matplotlib.pyplot as plt

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Angles for the rays (in radians)
alpha = np.radians(25)  # Lower ray
beta = np.radians(70)   # Upper ray

# Create theta values for the curves
theta = np.linspace(alpha, beta, 100)

# Try different candidate functions for the curves
# The curves should be smooth and monotonic in r as functions of theta

# Candidate 1: Linear in theta (simple)
def h1_linear(t):
    return 1.5 + 0.5 * (t - alpha) / (beta - alpha)

def h2_linear(t):
    return 2.8 + 0.5 * (t - alpha) / (beta - alpha)

# Candidate 2: Slightly curved (quadratic)
def h1_quad(t):
    s = (t - alpha) / (beta - alpha)  # Normalized to [0,1]
    return 1.3 + 0.8 * s + 0.2 * s**2

def h2_quad(t):
    s = (t - alpha) / (beta - alpha)
    return 2.5 + 0.6 * s + 0.3 * s**2

# Candidate 3: Sinusoidal variation (gives nice smooth curves)
def h1_sin(t):
    s = (t - alpha) / (beta - alpha)
    return 1.5 + 0.3 * np.sin(np.pi * s)

def h2_sin(t):
    s = (t - alpha) / (beta - alpha)
    return 2.8 + 0.4 * np.sin(np.pi * s)

# Looking at the original, the curves seem fairly smooth with slight bulge
# Let's use simple smooth curves that look good
h1 = h1_quad(theta)
h2 = h2_quad(theta)

# Convert to Cartesian for plotting
x1 = h1 * np.cos(theta)
y1 = h1 * np.sin(theta)
x2 = h2 * np.cos(theta)
y2 = h2 * np.sin(theta)

# Plot the shaded region (need to create polygon)
# Region vertices: along h1 from alpha to beta, then along h2 from beta to alpha
theta_region = np.concatenate([theta, theta[::-1]])
r_region = np.concatenate([h1, h2[::-1]])
x_region = r_region * np.cos(theta_region)
y_region = r_region * np.sin(theta_region)

ax.fill(x_region, y_region, color='lightgreen', alpha=0.7, edgecolor='none')

# Plot the curves
ax.plot(x1, y1, 'r-', linewidth=2, label='r = h1(theta)')
ax.plot(x2, y2, 'b-', linewidth=2, label='r = h2(theta)')

# Plot the rays
ray_length = 4
ax.plot([0, ray_length * np.cos(alpha)], [0, ray_length * np.sin(alpha)],
        'k-', linewidth=1)
ax.plot([0, ray_length * np.cos(beta)], [0, ray_length * np.sin(beta)],
        'k-', linewidth=1)

# Plot the coordinate axes
ax.axhline(y=0, color='k', linewidth=0.8)
ax.axvline(x=0, color='k', linewidth=0.8)
ax.arrow(0, 0, 3.5, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0, 3.5, head_width=0.1, head_length=0.1, fc='k', ec='k')

# Add labels
ax.text(ray_length * np.cos(beta) - 0.3, ray_length * np.sin(beta) + 0.2,
        r'$\theta = \beta$', fontsize=12)
ax.text(ray_length * np.cos(alpha) + 0.1, ray_length * np.sin(alpha) - 0.3,
        r'$\theta = \alpha$', fontsize=12)

# Curve labels
mid_idx = len(theta) // 2
ax.text(x1[mid_idx] - 0.5, y1[mid_idx] - 0.2, r'$r = h_1(\theta)$',
        fontsize=11, color='red')
ax.text(x2[mid_idx] + 0.2, y2[mid_idx] + 0.3, r'$r = h_2(\theta)$',
        fontsize=11, color='blue')

ax.set_xlim(-0.5, 4)
ax.set_ylim(-0.5, 4)
ax.set_aspect('equal')
ax.axis('off')

plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase4-polar-region/draft.png',
            dpi=150, bbox_inches='tight')
plt.close()

print("Draft saved to draft.png")
