import matplotlib.pyplot as plt
import numpy as np

# Analyzing the image:
# - f(x) blue: increasing, concave up on left side, starts below x-axis far left,
#   goes through origin area, rises steeply to upper right
#   Looks like a quadratic or cubic. At x=a (~2), f(a) is moderate (intersects g(x)).
#   At x=b (~4.5), f crosses h(x). At x=c (~7), f is high.
#
# - h(x) red: decreasing, starts high left, crosses f at ~x=b, ends moderate right
#   Looks like a decreasing function, concave shape
#   At x=c, h(x) = g(x) (they intersect at x=c)
#
# - g(x) green: starts high left, dips down to minimum around x=b, rises on right
#   U-shaped, concave up. Intersects f(x) at x=a, intersects h(x) at x=c
#
# Gray region: between the "upper envelope" of {f,h} and g(x), from x=a to x=c
# More precisely: from x=a to x=b, the top boundary is f(x) and bottom is g(x)
#   Wait, looking more carefully: at x=a, f=g (they intersect), and between a and b,
#   f(x) is above g(x). But h(x) is even higher until it crosses f at b.
#   The shaded region appears to be bounded above by min(f,h) or rather:
#   Actually looking again: the gray region is bounded:
#   - Above: by h(x) from a to ~b, then by f(x) from ~b to c? No...
#   Actually re-examining: the shaded area seems to be between the upper curves
#   and g(x). Let me look more carefully.
#
# At x=a: f(a) = g(a), h(a) is above both
# At x=b: f(b) = h(b), g(b) is below both
# At x=c: h(c) = g(c), f(c) is above both
#
# The shaded region is bounded:
# - From x=a to x=b: above by f(x), below by g(x) [f crosses g at a, f above g in between]
#   Wait no -- looking at the image again, h(x) is ABOVE f(x) from a to b.
#   The gray area seems to cover the region between the top curve and g(x).
#   But actually the shading looks like it's between f and g from a to b,
#   then between h and g from b to c. Actually that doesn't work either because
#   at b, f=h, and the shaded region is continuous.
#
# Let me just try: shaded region = area between max(f,h) on top... no.
# Actually looking at the image more carefully:
# The gray region looks like it's between f(x) on top (from a to b) and g(x) on bottom,
# then h(x) on top (from b to c) and g(x) on bottom. But wait, at x=a, f=g so the
# region starts as a point. And at x=c, h=g so it ends as a point. Between a and c,
# the "upper boundary" is whichever of f,h is relevant (they cross at b).
#
# Actually NO. Looking once more: between a and c, BOTH f and h are above g.
# The shaded region seems bounded above by the LOWER of f and h (i.e., min(f,h))
# and below by g. This makes sense:
# - At a: f=g, so region starts (min(f,h)=f=g)
# - a to b: f < h, so top is f, bottom is g
# - At b: f=h
# - b to c: h < f, so top is h, bottom is g
# - At c: h=g, so region ends
#
# This gives a nice lens/leaf shape for the shaded region!

# Let me set up coordinates: a=2, b=5, c=8
a, b, c = 2, 5, 8

x = np.linspace(-1, 10, 500)

# f(x): increasing, starts low, ends high
# Let's try f(x) = 0.08*(x-1)^2 + 0.3 shifted so it works
# Actually let's think about the constraints:
# f(a)=g(a), f(b)=h(b), f increases throughout

# g(x): U-shaped, minimum around x=b area
# g(a)=f(a), g(c)=h(c)

# h(x): decreasing from upper left to lower right
# h(b)=f(b), h(c)=g(c)

# Let me try simple functions:
# f(x) = 0.15*x^2 - 0.5*x + 1  (quadratic, opening up, increasing for x>~1.7)
# But we need f to be increasing in [a,c] and look like a smooth increasing curve.

# Let me try:
# f(x) = 0.1*(x-0)^2  -- simple parabola
# At x=2: f=0.4, at x=5: f=2.5, at x=8: f=6.4 -- too steep

# f(x) = 0.05*x^2 + 0.1*x - 0.5
# At x=2: 0.2+0.2-0.5=-0.1, at x=5: 1.25+0.5-0.5=1.25, at x=8: 3.2+0.8-0.5=3.5

# Let me just pick nice values and work backward.
# Target: at x=a=2, f=g=~1.0
#          at x=b=5, f=h=~2.5
#          at x=c=8, f=~4.0 (high)
# g(x) U-shaped: g(2)=1.0, g(min~5)=~0.5, g(8)=1.5
# h(x) decreasing: h(2)=~3.5, h(5)=2.5, h(8)=1.5

# f(x): increasing function through (2,1) and (5,2.5)
# slope = 1.5/3 = 0.5 -- could be linear but image shows curvature
# Let's try f(x) = a*x^2 + b*x + c
# f(2) = 1, f(5) = 2.5
# Make it slightly concave: f(x) = 0.05*x^2 + 0.2*x + 0.2
# f(2) = 0.2+0.4+0.2 = 0.8   close
# f(5) = 1.25+1.0+0.2 = 2.45  close
# f(8) = 3.2+1.6+0.2 = 5.0

# g(x): U-shaped, minimum around x=5
# g(x) = 0.1*(x-5)^2 + 0.3
# g(2) = 0.9+0.3 = 1.2  -- want ~1.0
# g(5) = 0.3
# g(8) = 0.9+0.3 = 1.2 -- want ~1.5

# Let me adjust: g(x) = 0.08*(x-4.5)^2 + 0.3 + 0.05*x
# g(2) = 0.08*6.25+0.3+0.1 = 0.5+0.3+0.1 = 0.9
# g(5) = 0.08*0.25+0.3+0.25 = 0.02+0.3+0.25 = 0.57
# g(8) = 0.08*12.25+0.3+0.4 = 0.98+0.3+0.4 = 1.68

# h(x): decreasing from left to right
# h(x) = -0.3*x + 3.5
# h(2) = 2.9, h(5) = 2.0, h(8) = 1.1 -- but we need h(5)=f(5) and h(8)=g(8)

# Let me reconsider and set exact intersection constraints.
# Let's say:
# At x=a=2: f(2) = g(2) = val1
# At x=b=5: f(5) = h(5) = val2
# At x=c=8: h(8) = g(8) = val3

# Choose: val1 = 1.0, val2 = 2.2, val3 = 1.5

# f(x): passes through (2, 1.0) and (5, 2.2), increasing, slightly concave up
# Try f(x) = A*(x-1) for simplicity? f(2)=A, f(5)=4A -> 4A=2.2 -> A=0.55 -> f(2)=0.55 no.
# Try f(x) = 0.06*x^2 + 0.16*x + 0.2
# f(2) = 0.24+0.32+0.2 = 0.76   not quite 1.0
# f(x) = 0.06*x^2 + 0.2*x + 0.12
# f(2) = 0.24+0.4+0.12 = 0.76   hmm
# f(x) = 0.08*x^2 + 0.1*x + 0.32
# f(2) = 0.32+0.2+0.32 = 0.84
# f(x) = 0.1*x^2 + 0*x + 0.6
# f(2) = 0.4+0.6 = 1.0    YES
# f(5) = 2.5+0.6 = 3.1    too high, want 2.2

# OK let me use exact constraints.
# f(x) = ax^2 + bx + c, f(2)=1.0, f(5)=2.2
# 4a+2b+c = 1.0
# 25a+5b+c = 2.2
# -> 21a+3b = 1.2 -> 7a+b = 0.4
# Choose a=0.04: b=0.4-0.28=0.12, c=1.0-0.16-0.24=0.6
# f(x)=0.04x^2+0.12x+0.6
# f(2)=0.16+0.24+0.6=1.0 YES
# f(5)=1.0+0.6+0.6=2.2 YES
# f(8)=2.56+0.96+0.6=4.12
# f(0)=0.6, f(-1)=0.04-0.12+0.6=0.52

# g(x): U-shaped, g(2)=1.0, g(8)=1.5, minimum around x=4-5
# g(x) = a(x-x0)^2 + g_min
# Symmetric would give x0=5, but we want g(2)>g(5) and g(8)>g(5) with g(8)>g(2)
# So minimum slightly left of center.
# g(x) = a(x-x0)^2 + d*x + e
# Or: g(x) = a*x^2 + b*x + c
# g(2)=1.0, g(8)=1.5
# 4a+2b+c=1.0, 64a+8b+c=1.5
# -> 60a+6b=0.5 -> 10a+b=1/12
# Choose vertex near x=4.5: vertex at x=-b/(2a)=4.5 -> b=-9a
# 10a-9a=1/12 -> a=1/12=0.0833
# b=-9/12=-0.75
# c=1.0-4(1/12)-2(-0.75)=1.0-1/3+1.5=2.167
# g(x)=0.0833x^2 - 0.75x + 2.167
# g(2)=0.333-1.5+2.167=1.0 YES
# g(5)=2.083-3.75+2.167=0.5
# g(8)=5.333-6.0+2.167=1.5 YES
# g(0)=2.167

# h(x): decreasing, h(5)=2.2, h(8)=1.5
# Could be linear or slightly curved
# Linear: h(x) = -0.233x + 3.367
# h(2) = -0.467+3.367 = 2.9
# h(5) = -1.167+3.367 = 2.2 YES
# h(8) = -1.867+3.367 = 1.5 YES
# But the image shows h(x) as curved (concave down). Let's add slight curvature.
# h(x) = ax^2 + bx + c, h(5)=2.2, h(8)=1.5
# Make it concave down: a<0
# Choose a=-0.02:
# 25(-0.02)+5b+c=2.2 -> 5b+c=2.7
# 64(-0.02)+8b+c=1.5 -> 8b+c=2.78
# -> 3b=0.08 -> b=0.0267, c=2.7-0.133=2.567
# h(x) = -0.02x^2 + 0.0267x + 2.567
# h(2) = -0.08+0.053+2.567 = 2.54
# h(5) = -0.5+0.133+2.567 = 2.2 YES
# h(8) = -1.28+0.213+2.567 = 1.5 YES
# h(0) = 2.567
# h(-1) = -0.02-0.0267+2.567 = 2.52  -- should be higher on left
# This doesn't decrease steeply enough from left.

# Let me try a steeper curve for h:
# h(x) = -0.04x^2 + 0.12x + 2.52
# h(2) = -0.16+0.24+2.52 = 2.6
# h(5) = -1.0+0.6+2.52 = 2.12  want 2.2
# Adjust: h(x) = -0.04x^2 + bx + c
# h(5) = -1.0+5b+c = 2.2 -> 5b+c=3.2
# h(8) = -2.56+8b+c = 1.5 -> 8b+c=4.06
# 3b=0.86 -> b=0.287, c=3.2-1.433=1.767
# h(x) = -0.04x^2+0.287x+1.767
# h(2) = -0.16+0.573+1.767 = 2.18
# h(0) = 1.767
# h(-1) = -0.04-0.287+1.767 = 1.44 -- this goes DOWN to left, bad
# The concavity is wrong with a<0 for getting a high value on the left.

# For h to start high on the left and decrease, with concave shape as in image:
# Actually looking at the image again, h appears to be a gentle S or just a smooth
# decreasing curve. Let me try a gentler approach.
# h(x) = -0.3x + 3.7  (linear first, can curve later in TikZ)
# h(2) = 3.1, h(5) = 2.2, h(8) = 1.3
# But we need h(8) = g(8) = 1.5
# h(x) = slope*(x) + intercept
# h(5)=2.2, h(8)=1.5: slope = (1.5-2.2)/(8-5) = -0.233
# h(x) = -0.233x + 3.367
# h(2) = 2.9

# For the image, h seems to flatten as it goes right (concave up for decreasing)
# Try: h(x) = A/x + B or h(x) = A*exp(-kx) + B
# h(5) = 2.2, h(8) = 1.5
# A*exp(-5k)+B = 2.2, A*exp(-8k)+B = 1.5
# Try k=0.1: A*(e^-0.5)+B=2.2, A*(e^-0.8)+B=1.5
# A*(0.6065-0.4493) = 0.7 -> A=4.45
# B=2.2-4.45*0.6065=2.2-2.7=-0.5
# h(x) = 4.45*exp(-0.1x) - 0.5
# h(2) = 4.45*exp(-0.2)-0.5 = 4.45*0.8187-0.5 = 3.14
# h(0) = 4.45-0.5 = 3.95
# h(-1) = 4.45*exp(0.1)-0.5 = 4.45*1.105-0.5 = 4.42  good, high on left

# OK this is getting complex. Let me just pick nice simple functions and plot them.

fig, ax = plt.subplots(1, 1, figsize=(12, 7))

x = np.linspace(-2, 11, 500)

# Simple approach: just define nice-looking curves
# f(x) = 0.04x^2 + 0.12x + 0.6
f = 0.04*x**2 + 0.12*x + 0.6

# g(x) = 0.0833x^2 - 0.75x + 2.167
g = (1/12)*x**2 - 0.75*x + 2.167

# h(x) = linear: -0.233x + 3.367
h_lin = -0.2333*x + 3.367

ax.plot(x, f, 'b-', linewidth=2, label='f(x)')
ax.plot(x, g, 'g-', linewidth=2, label='g(x)')
ax.plot(x, h_lin, 'r-', linewidth=2, label='h(x)')

# Mark intersection points
ax.axvline(x=2, color='gray', linewidth=0.5, linestyle='-')
ax.axvline(x=5, color='gray', linewidth=0.5, linestyle='-')
ax.axvline(x=8, color='gray', linewidth=0.5, linestyle='-')

# Shade between min(f,h) and g from x=a to x=c
x_shade = np.linspace(2, 8, 300)
f_shade = 0.04*x_shade**2 + 0.12*x_shade + 0.6
g_shade = (1/12)*x_shade**2 - 0.75*x_shade + 2.167
h_shade = -0.2333*x_shade + 3.367
upper = np.minimum(f_shade, h_shade)
ax.fill_between(x_shade, g_shade, upper, alpha=0.3, color='gray')

ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)
ax.set_xlim(-2, 11)
ax.set_ylim(-1, 5)
ax.legend()
ax.set_title('Draft: TestCase3')

plt.savefig('/Users/mingheiwong/Desktop/MathThermoCourseLatex/TikzPlayground/TestCase3-opus/draft.png', dpi=150)
plt.close()
print("Draft saved.")

# Print key values
print(f"f(2)={0.04*4+0.12*2+0.6:.2f}, f(5)={0.04*25+0.12*5+0.6:.2f}, f(8)={0.04*64+0.12*8+0.6:.2f}")
print(f"g(2)={(1/12)*4-0.75*2+2.167:.2f}, g(5)={(1/12)*25-0.75*5+2.167:.2f}, g(8)={(1/12)*64-0.75*8+2.167:.2f}")
print(f"h(2)={-0.2333*2+3.367:.2f}, h(5)={-0.2333*5+3.367:.2f}, h(8)={-0.2333*8+3.367:.2f}")
