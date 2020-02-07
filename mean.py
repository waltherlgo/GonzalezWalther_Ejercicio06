import numpy as np
import matplotlib.pyplot as plt
x = [4.6, 6.0, 2.0, 5.8] 
sigma = [2.0, 1.5, 5.0, 1.0]
def probx(mu,sig,x):
    Px=1/(sig*np.sqrt(2*np.pi))*np.exp(-1/2*((x-mu)/sig)**2)
    return np.log(Px)
muL=np.linspace(0,10,1000)
LPmu=[np.sum([probx(mu,sigma[i],x[i]) for i in range (len(x))]) for mu in muL]
LPmu=np.array(LPmu)
sD=(LPmu[2:-1]-2*LPmu[1:-2]+LPmu[0:-3])*100*100
sig=1/np.sqrt(-sD[np.argmax(LPmu)])
Mu0=muL[np.argmax(LPmu)]
Pmu=np.exp(LPmu)
Pmu=Pmu/(sum(Pmu))*100
plt.title(r'$\mu=$%4.3f'%Mu0+r'$\pm$%4.3f'%sig)
plt.plot(muL,Pmu)
plt.axvline(x=Mu0,color='r',linestyle='--')
plt.xlabel(r'$\mu$')
plt.ylabel('Posterior')
plt.savefig('mean.png')
plt.show()