import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

x = np.linspace(0, 1, 500)

# Binodal: wider dome, symmetric about x=0.5
# Looks like it starts near x~0.05 and ends near x~0.95
# Using a parabolic form: T_bin = A * x*(1-x), or T_bin = A*(0.25 - (x-0.5)^2)
# The binodal looks quite rounded at the top, so parabola-like
# Maximum at x=0.5, zeros at x=0 and x=1 for x*(1-x)
# But in the image, the binodal appears to hit zero slightly inside (around 0.05 and 0.95)
# Let's try: T_bin = A * (x - a)*(b - x) for a~0.05, b~0.95

# Actually looking more carefully, the binodal curve goes to zero temperature
# at approximately x=0.05 and x=0.95, but the curve is quite tall

# Try binodal: 4*x*(1-x) rescaled
# The shape looks more like sin(pi*x) actually - rounder at top
T_max_bin = 1.0  # normalized

# Option 1: parabolic
T_bin_parab = 4 * T_max_bin * x * (1 - x)

# Option 2: sin
T_bin_sin = T_max_bin * np.sin(np.pi * x)

# The spinodal is narrower, also symmetric about 0.5
# Zeros near x=0.2 and x=0.8
# Max near x=0.5 at about 90% of binodal max

T_max_spin = 0.92 * T_max_bin

# Spinodal parabolic: centered at 0.5, zeros at 0.2 and 0.8
# T_spin = A * (x - 0.2)*(0.8 - x) for x in [0.2, 0.8]
# Maximum of (x-0.2)(0.8-x) at x=0.5 is (0.3)(0.3) = 0.09
# So A = T_max_spin / 0.09

A_spin = T_max_spin / 0.09
T_spin_parab = np.where((x >= 0.2) & (x <= 0.8), A_spin * (x - 0.2) * (0.8 - x), 0)

# Spinodal sin: sin(pi*(x-0.2)/0.6) for x in [0.2, 0.8]
T_spin_sin = np.where((x >= 0.2) & (x <= 0.8),
                       T_max_spin * np.sin(np.pi * (x - 0.2) / 0.6), 0)

# Plot both options
ax.plot(x, T_bin_parab, 'b-', linewidth=2, label='Binodal (parabolic)')
ax.plot(x, T_bin_sin, 'b--', linewidth=2, label='Binodal (sin)')
ax.plot(x, T_spin_parab, 'r-', linewidth=2, label='Spinodal (parabolic)')
ax.plot(x, T_spin_sin, 'r--', linewidth=2, label='Spinodal (sin)')

ax.set_xlabel('$x_1$')
ax.set_ylabel('Temperature')
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.2)

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase2-opus/draft.png', dpi=150)
plt.close()
print("Draft saved.")
