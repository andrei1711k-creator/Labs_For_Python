import numpy as np
import matplotlib.pyplot as plt



def main():
    x_deg = np.linspace(-360, 360, 4000)
    x_rad = np.radians(x_deg)

    f = np.exp(np.cos(x_rad)) + np.log(np.cos(0.6 * x_rad)**2 + 1) * np.sin(x_rad)
    h = -np.log((np.cos(x_rad) + np.sin(x_rad))**2 + 2.5) + 10

    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axs[0].plot(x_deg, f, label="f(x)", color='tab:blue')
    axs[0].set_title("График функции f(x)")
    axs[0].grid(True)
    axs[0].legend()

    axs[1].plot(x_deg, h, label="h(x)", color='tab:orange')
    axs[1].set_title("График функции h(x)")
    axs[1].grid(True)
    axs[1].legend()

    axs[1].set_xlabel("x (в градусах)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
