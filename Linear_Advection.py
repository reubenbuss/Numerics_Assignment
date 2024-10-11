import numpy as np 
import matplotlib.pyplot as plt

#setup parameters 
u = 1
nx= 40
x = np.linspace(0,1,nx+1)
nt= 80
dx=1/nx
dt=1/nt

# The initial conditions 
phi = np.where(x%1 < 0.5, np.power(np.sin(2*x*np.pi),2),0)
#phi = np.where(0, x > 0.05 and x < 0.5, 0.5, 0)
phiOld = phi.copy()

#plot the initial conditions 
plt.plot(x,phi,'k',label='Inital Conditions')
plt.legend(loc='best')
plt.ylabel('$\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.ylim([0,1])
plt.pause(1)

def analytic(x,u,t):
    y = x-u*t
    return np.where(y%1 < 0.5, np.power(np.sin(2*y*np.pi),2),0)
    #return np.where(x%1 < 0.5, 0.5,0)

#loop over all time steps 
for n in range(nt):
    for j in range(1,nx+1):
        phi[j] = phiOld[j] - u*dt*(phiOld[j]-phiOld[j-1])/dx
    phi[0] = phi[-1]
    phiOld = phi.copy()
    plt.cla()
    plt.plot(x,phi,'b',label='Finite Difference ' + str(n*dt))
    plt.plot(x,analytic(x,u,n/nt),'r',label='Analytic ' + str(n*dt))
    plt.legend(loc = 'best')
    plt.ylabel('$\phi$')
    plt.ylim([0,1])
    plt.pause(0.001)
plt.show()


