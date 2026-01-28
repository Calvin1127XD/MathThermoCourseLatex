"""
Draft 2: Refine the boundary curve to better match the original.

The original has:
- Curve starts at left edge near the bottom (y ~ 1/6 of height)
- Very steep S-shape: rises sharply from bottom-left to about 2/3 height at x=2.5
- Then curves back down to about 1/3 height at x=5
- Small bump/hump near x=6.5 going up slightly
- Exits right edge at about 1/3 height (slightly below center)

The box in the original appears slightly wider than tall (aspect ratio ~4:3).
"""
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

box_w, box_h = 8, 6

for ax_idx, ax in enumerate(axes):
    rect = plt.Rectangle((0, 0), box_w, box_h, linewidth=3, edgecolor='black', facecolor='white')
    ax.add_patch(rect)

    x = np.linspace(0, box_w, 300)

    if ax_idx == 0:
        # Version A: steeper S-curve using atan or tanh transition
        # Transition from low to high centered around x=2
        transition = 1.5 * (np.tanh(2.0*(x - 2.0)) + 1) / 2  # goes from ~0 to ~1.5
        # Overall rising baseline
        base = 1.0
        # Small oscillation on top
        osc = -0.5 * np.cos(0.7 * x)
        # Bump near right
        bump = 0.5 * np.exp(-((x - 6.5)**2) / 0.8)
        # Dip in the middle
        dip = -0.8 * np.exp(-((x - 4.5)**2) / 1.5)

        y_boundary = base + transition + osc + bump + dip
        ax.set_title("Version A: tanh transition")

    else:
        # Version B: More aggressive S-shape
        # The curve in the original looks like it goes:
        # - from (0, 0.8) very steeply up to (2, 4.5)
        # - then down to (5, 2.0)
        # - small bump at (6.5, 3.0)
        # - exit at (8, 2.5)

        # Use a combination: steep sigmoid + sinusoidal
        sigmoid = 3.0 / (1 + np.exp(-3*(x - 1.5)))  # steep rise centered at x=1.5
        wave = -0.8 * np.sin(0.8*(x - 2.0))
        bump = 0.4 * np.exp(-((x - 6.5)**2) / 0.6)

        y_boundary = 0.5 + sigmoid + wave + bump - 1.0
        # Adjust so it starts low and ends mid
        ax.set_title("Version B: sigmoid + wave")

    y_boundary = np.clip(y_boundary, 0.1, box_h - 0.1)

    epsilon = 0.5
    ax.fill_between(x, y_boundary - epsilon, y_boundary + epsilon,
                    color='gray', alpha=0.3, zorder=2)
    ax.plot(x, y_boundary, 'k-', linewidth=2.5, zorder=3)

    ax.text(1.3, 5, r'$\phi = 1$', fontsize=16, ha='center', va='center')
    ax.text(6, 5, 'Phase 1', fontsize=16, ha='center', va='center')
    ax.text(1.3, 0.8, r'$\phi = -1$', fontsize=16, ha='center', va='center')
    ax.text(6, 0.8, 'Phase 2', fontsize=16, ha='center', va='center')

    # Epsilon arrow
    idx = int(2.8 / box_w * 300)
    arrow_y_c = y_boundary[idx]
    ax.annotate('', xy=(2.8, arrow_y_c + epsilon), xytext=(2.8, arrow_y_c - epsilon),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax.text(3.1, arrow_y_c, r'$\varepsilon$', fontsize=18, color='red', ha='left', va='center')

    ax.set_xlim(-0.3, box_w + 0.3)
    ax.set_ylim(-0.3, box_h + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')

    print(f"Version {'A' if ax_idx==0 else 'B'}:")
    print(f"  y at x=0: {y_boundary[0]:.2f}")
    print(f"  y at x=2: {y_boundary[int(2/8*300)]:.2f}")
    print(f"  y at x=4: {y_boundary[int(4/8*300)]:.2f}")
    print(f"  y at x=6: {y_boundary[int(6/8*300)]:.2f}")
    print(f"  y at x=8: {y_boundary[-1]:.2f}")

plt.tight_layout()
plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase1-opus/draft2.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("Draft 2 saved.")
