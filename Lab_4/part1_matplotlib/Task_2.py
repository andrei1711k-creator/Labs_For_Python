import numpy as np
import matplotlib.pyplot as plt

x_deg = np.linspace(-10,10,100)


f=5/(x_deg**2 - 9)

fig, axs = plt.subplots(1, 1, figsize=(10, 8), sharex=True)

axs.plot(x_deg, f, label="f(x)", color='tab:blue')
axs.set_title("График функции f(x)")
axs.grid(True)
axs.legend()

plt.xlabel("x (в градусах)")
plt.tight_layout()
plt.show()
