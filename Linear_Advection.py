import numpy as np 
import matplotlib.pyplot as plt
cmap = plt.get_cmap('Paired')


#setup parameters 
u = 1
nx= 100
x = np.linspace(0,1,nx+1)
nt= 500
dx=1/nx
dt=1/nt
c = u*dt/dx

def create_phi(y):
    phi1 = np.where(y%1 < 0.5, np.power(np.sin(2*y*np.pi),2),0)
    #phi2 = np.where((0.1 < x) & (x < 0.3), 1,0)
    return phi1#+phi2

def plot_intial(phi):
    #plot the initial conditions 
    plt.plot(x,phi,'k',label='Inital Conditions')
    plt.legend(loc='best')
    plt.ylabel('$\\phi$')
    plt.axhline(0,linestyle=':',color='black')
    plt.ylim([-0.1,1.1])
    plt.pause(1)

def analytic(t):
    return create_phi(x-u*t)

def FTBS_scheme(phi):
    phiOld = phi.copy()
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
    phis = [phi,analytic(x,u,dt)] #Initial conditions 
    for n in range(2,nt):
        for j in range(1,nx):
            phi[j] = phis[0][j] - c*(phis[1][j+1]-phis[1][j-1])
        phi[0] = phis[0][0] - c*(phis[1][1]-phis[1][-2])
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

#Hillary here!    
def Hilary_CTCS_scheme():
    phis = [analytic(0),analytic(dt)] #Initial conditons
    plt.plot(x,phis[0],c=cmap(0),label='Finite Difference Initial')
    plt.plot(x,phis[1],c=cmap(1),label='Analytic Initial',linestyle='dashed')
    phi = np.linspace(0,1,nx+1)
    for n in range(2,nt+1):
        for j in range(1,nx):
            phi[j] = phis[0][j] - c*(phis[1][j+1]-phis[1][j-1])
        phi[0] = phis[0][0] - c*(phis[1][1]-phis[1][-2])
        phi[-1] = phi[0]
        phis.append(phi)
        del phis[:-2] #Remove all but the final two elements from the list of phi states. 
        if n==450: #to show the speed difference at non cyclic time
            plt.plot(x,phis[0],c=cmap(2),label='Finite Difference ' + str(n*dt))
            plt.plot(x,analytic(n/nt),c=cmap(3),label='Analytic ' + str(n*dt),linestyle='dashed')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=2)
    plt.title(f'Courant number {c}')
    plt.ylabel('$\\phi$')
    plt.ylim([-0.1,1.1])
    plt.show()
    
def CTCS_scheme_steps(phi,steps):
    divider = nt/steps
    phis = [phi,analytic(x,u,dt)] #create a list of phi states 
    print(phis[0][0])
    for n in range(2,nt):
        for j in range(1,nx):
            phi[j] = phis[0][j] - c*(phis[1][j+1]-phis[1][j-1])
        phi[0] = phis[0][0] - c*(phis[1][1]-phis[1][-2])
        phi[-1] = phi[0]
        phis.append(phi)
        del phis[:-2] #Remove all but the final two elements from the list of phi states. 
        if n==2:
            plt.plot(x,phi,c=cmap(0),label='Finite Difference ' + str(n*dt))
            plt.plot(x,analytic(x,u,n/nt),c=cmap(1),label='Analytic ' + str(n*dt))
        elif n%divider == 0:
            colour = int(round(n//(divider//2),0))
            plt.plot(x,phi,c=cmap(colour),label='Finite Difference ' + str(n*dt))
            plt.plot(x,analytic(x,u,n/nt),c=cmap(colour),label='Analytic ' + str(n*dt),linestyle='dashed')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=2)
    plt.title(f'Courant number {c}')
    plt.ylabel('$\\phi$')
    plt.ylim([-0.1,1.1])
    plt.show()
    
def FTCS_scheme(phi):
    phiOld = phi.copy()
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


#CTCS_scheme_steps(create_phi(x),4)   
Hilary_CTCS_scheme()
#FTBS_scheme(create_phi(x))
#FTCS_scheme(create_phi(x))
#loop over all time steps 



