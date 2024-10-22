import numpy as np
import matplotlib.pyplot as plt
import Linear_Advection as LA

# Setup parameters
u = 1
nx = 100
x = np.linspace(0, 1, nx + 1)
nt = 500
dx = 1 / nx
dt = 1 / nt
c = u * dt / dx

def create_phi(y):
    return np.where(y % 1 < 0.5, np.power(np.sin(2 * y * np.pi), 2), 0)
     

def analytic(x, u, t):
    # Example analytical solution (modify as needed)
    return create_phi(x - u * t)

def CTCS_scheme(phi):
    phis = [phi.copy(), analytic(x, u, dt)]  # Initial conditions
    for n in range(2, nt):
        for j in range(1, nx):
            phi[j] = phis[0][j] - c * (phis[1][j + 1] - phis[1][j - 1])
        phi[0] = phis[0][0] - c * (phis[1][1] - phis[1][-2])
        phi[-1] = phi[0]
        
        phis.append(phi.copy())
        
        plt.cla()
        plt.plot(x, phi, 'b', label='Finite Difference ' + str(n * dt))
        plt.plot(x, analytic(x, u, n * dt), 'r', label='Analytic ' + str(n * dt))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=2)
        plt.title(f'Courant number {c}')
        plt.ylabel('$\\phi$')
        plt.ylim([-0.1, 1.1])
        plt.pause(0.01)
        
        del phis[:-2]  # Remove all but the final two elements from the list of phi states. 
    plt.show()

# Initialize phi and run the scheme
# phi = create_phi(x)
# CTCS_scheme(phi)
#LA.CTCS_scheme_plotting_all(create_phi(x))


phis = LA.CTCS_points(x,u,nx,nt)
plt.plot(x, phis[0], 'b', label='Start')
plt.plot(x, phis[-1], 'r', label='Finish')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=2)
plt.title(f'Courant number {c}')
plt.ylabel('$\\phi$')
plt.show()

# LA.CTCS_points(x,u,nx,nt,True)