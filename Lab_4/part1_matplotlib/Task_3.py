
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, PathPatch
from matplotlib.path import Path
import numpy as np


fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect("equal")
ax.axis("off")


head = Circle((0, 0), 2.5, color="#FFA500", ec="black", lw=2)
ax.add_patch(head)


left_ear = Polygon([[-1.8, 2.2], [-2.7, 3.5], [-1.2, 3.0]], color="#FFA500", ec="black", lw=2)
right_ear = Polygon([[1.8, 2.2], [2.7, 3.5], [1.2, 3.0]], color="#FFA500", ec="black", lw=2)
ax.add_patch(left_ear)
ax.add_patch(right_ear)


stripes = [
        [(-1.0, 2.0), (0, 1.5), (1.0, 2.0)],
        [(-1.3, 1.4), (0, 1.0), (1.3, 1.4)],
        [(-1.6, 0.8), (0, 0.6), (1.6, 0.8)],
    ]
for pts in stripes:
    path_data = [(Path.MOVETO, pts[0]), (Path.CURVE3, pts[1]), (Path.CURVE3, pts[2])]
    codes, verts = zip(*path_data)
    path = Path(verts, codes)
    patch = PathPatch(path, lw=6, color="black", capstyle='round')
    ax.add_patch(patch)


cheek_stripes_left = [
        [(-2.0, 0.6), (-1.2, 0.3)],
        [(-2.1, 0.0), (-1.3, -0.2)],
        [(-2.0, -0.7), (-1.4, -0.8)]
    ]
cheek_stripes_right = [
        [(2.0, 0.6), (1.2, 0.3)],
        [(2.1, 0.0), (1.3, -0.2)],
        [(2.0, -0.7), (1.4, -0.8)]
    ]

for side in cheek_stripes_left + cheek_stripes_right:
        ax.plot(*zip(*side), color="black", lw=5, solid_capstyle='round')


left_eye = Circle((-0.9, 0.5), 0.35, color="white", ec="black", lw=1.5)
right_eye = Circle((0.9, 0.5), 0.35, color="white", ec="black", lw=1.5)
ax.add_patch(left_eye)
ax.add_patch(right_eye)
ax.add_patch(Circle((-0.9, 0.5), 0.15, color="black"))
ax.add_patch(Circle((0.9, 0.5), 0.15, color="black"))


nose = Polygon([[0, 0.1], [-0.3, -0.4], [0.3, -0.4]], color="black")
ax.add_patch(nose)


ax.plot([-0.3, 0, 0.3], [-0.6, -0.9, -0.6], color="black", lw=2)


for y in [-0.4, -0.6, -0.8]:
        ax.plot([-2.3, -0.6], [y, y], color="black", lw=1)
        ax.plot([2.3, 0.6], [y, y], color="black", lw=1)


ax.text(0, -3.6, "Ай, тигр!", fontsize=26, fontweight="bold",
            ha="center", color="#FF6600", family="Comic Sans MS")

plt.show()

