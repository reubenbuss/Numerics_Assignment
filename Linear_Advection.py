import numpy as np 
import matplotlib.pyplot as plt

#setup parameters 
u = 1
nx= 100
x = np.linspace(0,1,nx+1)
nt= 500
dx=1/nx
dt=1/nt
c = u*dt/dx

# The initial conditions 
def create_phi(x):
    phi1 = np.where(x > 0.5, np.power(np.sin(2*x*np.pi),2),0)
    #phi2 = np.where((0.1 < x) & (x < 0.3), 1,0)
    return phi1#+phi2

#phi = np.where(0, x > 0.05 and x < 0.5, 0.5, 0)
phi = create_phi(x)
phiOld = phi.copy()

#plot the initial conditions 
plt.plot(x,phi,'k',label='Inital Conditions')
plt.legend(loc='best')
plt.ylabel('$\\phi$')
plt.axhline(0,linestyle=':',color='black')
plt.ylim([-0.1,1.1])
plt.pause(1)

def analytic(x,u,t):
    y = x-u*t
    return create_phi(y%1)

def FTBS_scheme(phiOld):
    for n in range(nt):
        for j in range(1,nx+1):
            phi[j] = phiOld[j] - c*(phiOld[j]-phiOld[j-1])
        phi[0] = phi[-1]
        phiOld = phi.copy()
        plt.cla()
        plt.plot(x,phi,'b',label='Finite Difference ' + str(n*dt))
        plt.plot(x,analytic(x,u,n/nt),'r',label='Analytic ' + str(n*dt))
        plt.legend(loc = 'best')
        plt.ylabel('$\\phi$')
        plt.ylim([-0.1,1.1])
        plt.pause(0.01)
    plt.show()

def CTCS_scheme(phi):
    phis = [phi,analytic(x,u,dt)] #create a list of phi states 
    print(phis[0][0])
    for n in range(2,nt):
        for j in range(1,nx):
            phi[j] = phis[0][j] - c/2*(phis[1][j+1]-phis[1][j-1])
        phi[0] = phis[0][0] - c/2*(phis[1][1]-phis[1][-2])
        phi[-1] = phi[0]
        phis.append(phi)
        plt.cla()
        plt.plot(x,phi,'b',label='Finite Difference ' + str(n*dt))
        plt.plot(x,analytic(x,u,n/nt),'r',label='Analytic ' + str(n*dt))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=2)
        plt.title(f'Courant number {c}')
        plt.ylabel('$\\phi$')
        plt.ylim([-0.1,1.1])
        plt.pause(0.01)
        del phis[:-2] #Remove all but the final two elements from the list of phi states. 
    plt.show()
    
def FTCS_scheme(phiOld):
    for n in range(nt):
        for j in range(1,nx):
            phi[j] = phiOld[j] - c/2*(phiOld[j+1]-phiOld[j-1])
        phi[0] = phiOld[0] - c/2*(phiOld[1]-phiOld[-2])
        phi[-1] = phi[0]
        phiOld = phi.copy()
        plt.cla()
        plt.plot(x,phi,'b',label='Finite Difference ' + str(n*dt))
        plt.plot(x,analytic(x,u,n/nt),'r',label='Analytic ' + str(n*dt))
        plt.legend(loc = 'best')
        plt.ylabel('$\\phi$')
        plt.ylim([-0.1,1.1])
        plt.pause(0.01)
    plt.show()  
    
  
    
#CTCS_scheme(phi)
#FTBS_scheme(phiOld)
FTCS_scheme(phiOld)
#loop over all time steps 



