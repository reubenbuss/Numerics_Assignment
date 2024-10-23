import numpy as np
import matplotlib.pyplot as plt
import Linear_Advection as LA


# Setup parameters
nx = 100
nt = 500
#Constants
u=1
x = np.linspace(0, 1, nx + 1)
#running the code
c = u*nx/nt
phis = LA.CTCS_points(x,u,nx,nt)
plt.plot(x, phis[0], 'b', label='Start')
plt.plot(x, phis[-1], 'r', label='Finish',linestyle='dashed')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, ncol=2)
plt.title(f'Courant Number {c}')
plt.ylabel('$\\phi$')
plt.savefig(f'Plots/nx_{nx}nt_{nt}c{str(c).replace('.','_')}.svg')
plt.show()

#print(LA.integration(phis,nx))