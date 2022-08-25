import matplotlib.pylplot as plt
import numpy as np

# Quadratic drag horizontal motion
# Plot velocity over time

# Define velocity


def velocity(t, c=0.2, m=80, v0=20):
    """
    Calculate velocity of cyclist under ONLY quadratic drag
    v(t) = v0 / (1 + c*v0*t/m)
    :param t: time (s)
    :param c: drag constant (kg/m)
    :param m: mass (kg)
    :param v0: initial speed (m/s)
    :return: velocity (m/s)
    """
    # Calculate time constant
    tau = m / (c * v0)
    # Calculate and return velocity
    vt = v0 / (1 + (t / tau))
    return vt


if __name__ == '__main__':
    # Set range of t
    t = np.linspace(0, 20, 1000)
    v = velocity(t)
    # Begin plotting
    fig = plt.figure()
    plt.plot(t, v)
    plt.savefig("2d.png")
