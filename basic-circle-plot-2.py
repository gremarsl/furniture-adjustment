import matplotlib.pyplot as plt
import matplotlib.patches as pat

fig, ax = plt.subplots(1)
circle = pat.Circle(xy=(0, 0), radius=1)

ax.add_patch(circle)
plt.xlim(right=1)  # xmax is your value
plt.xlim(left=-1)  # xmin is your value
plt.ylim(top=1)  # ymax is your value
plt.ylim(bottom=-1)  # ymin is your value
plt.plot()
plt.show()