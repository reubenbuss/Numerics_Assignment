import numpy as np 
import matplotlib.pyplot as plt
cmap = plt.get_cmap('Paired')


#setup parameters 
# u = 1
# nx= 100
# x = np.linspace(0,1,nx+1)
# nt= 500
# dx=1/nx
# dt=1/nt
# c = u*dt/dx

def create_phi(y):
    return np.where((y%1 > 0.25) & (y%1 < 0.75), np.power(np.sin(2*(y-0.25)*np.pi),2),0)

def plot_intial():
    #plot the initial conditions
    phi = create_phi(x.copy())
    plt.plot(x,phi,'k',label='Inital Conditions')
    plt.legend(loc='best')
    plt.ylabel('$\\phi$')
    plt.axhline(0,linestyle=':',color='black')
    plt.ylim([-0.1,1.1])
    plt.pause(1)

def analytic(x,u,t):
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

def CTCS_scheme_plotting_all(phi):
    phis = [phi,analytic(dt)] #Initial conditions 
    for n in range(2,nt):
        for j in range(1,nx):
            phi[j] = phis[0][j] - c*(phis[1][j+1]-phis[1][j-1])
        phi[0] = phis[0][0] - c*(phis[1][1]-phis[1][-2])
        phi[-1] = phi[0]
        phis.append(phi.copy())
        plt.cla()
        plt.plot(x,phi,'b',label='Finite Difference ' + str(n*dt))
        plt.plot(x,analytic(n/nt),'r',label='Analytic ' + str(n*dt))
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=2)
        plt.title(f'Courant number {c}')
        plt.ylabel('$\\phi$')
        plt.ylim([-0.1,1.1])
        plt.pause(0.01)
        del phis[:-2] #Remove all but the final two elements from the list of phi states. 
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

def CTCS_points(x,u,nx,nt,plot=False):
    dx=1/nx
    dt=1/nt
    c = u*dt/dx
    phi = create_phi(x)
    initial_phi=phi.copy()
    print('you smell')
    plot(x,initial_phi,c='k')
    phis = [initial_phi,analytic(x,u,dt)] #Initial conditions 
    for n in range(2,nt):
        for j in range(1,nx):
            phi[j] = phis[-2][j] - c*(phis[-1][j+1]-phis[-1][j-1])
        phi[0] = phis[-2][0] - c*(phis[-1][1]-phis[-1][-2])
        phi[-1] = phi[0]
        phis.append(phi.copy())
    if plot == True:
        for i in range(0,nt):
            plt.cla()
            plt.plot(x,phis[i],'b',label='Finite Difference ' + str(n*dt))
            plt.plot(x,analytic(x,u,i/nt),'r',label='Analytic ' + str(n*dt))
            plt.legend(loc = 'best')
            plt.ylabel('$\\phi$')
            plt.ylim([-0.1,1.1])
            plt.pause(0.01)
        plt.show()
    else:
        return phis
  
#CTCS_scheme_steps(create_phi(x),4)   
#CTCS_scheme_plotting_all(create_phi(x))
#FTBS_scheme(create_phi(x))
#FTCS_scheme(create_phi(x))
#loop over all time steps 





