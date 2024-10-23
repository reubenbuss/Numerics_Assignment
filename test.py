import numpy as np
import matplotlib.pyplot as plt
import Linear_Advection as LA

# Setup parameters
u = 1
nx = 100
x = np.linspace(0, 1, nx + 1)
nt = 500

phis = LA.CTCS_points(x,u,nx,nt)
plt.plot(x, phis[0], 'b', label='Start')
plt.plot(x, phis[-1], 'r', label='Finish')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=2)
plt.title(f'First and Last')
plt.ylabel('$\\phi$')
plt.show()

#print(LA.integration(phis,nx))
