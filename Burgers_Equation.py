# This is the start of my code for the burger's equation

import numpy as np
import matplotlib.pyplot as plt

# Parameters
nx = 101  # number of spatial points
nt = 100  # number of time steps
dx = 2 / (nx - 1)  # spatial step size
nu = 0.07  # viscosity
dt = dx * nu  # time step size

# Initial condition
u = np.ones(nx)
u[int(0.5 / dx):int(1 / dx + 1)] = 2  # initial condition: u = 2 between 0.5 and 1

# Time-stepping loop
for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = (un[i] - un[i] * dt / dx * (un[i] - un[i - 1]) +
                nu * dt / dx**2 * (un[i + 1] - 2 * un[i] + un[i - 1]))

# Plotting the result
    plt.cla()
    plt.plot(np.linspace(0, 2, nx), u)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.title('1D Viscous Burgers\' Equation')
    plt.pause(0.05)

plt.show()
