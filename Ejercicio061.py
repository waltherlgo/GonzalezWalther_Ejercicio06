import numpy as np
import matplotlib.pyplot as plt
sig=0.3
xl = np.random.normal(0.8, sig, 1000)
muL=np.linspace(0.5,1,100)
def probx(mu,sig,x):
    Px=1/(sig*np.sqrt(2*np.pi))*np.exp(-1/2*((x-mu)/sig)**2)
    return Px
count=0
Pmu=[np.prod(probx(mu,sig,xl) ) for mu in muL]
plt.plot(muL,Pmu/(np.sum(Pmu))*1000)
Mu=muL[np.argmax(Pmu)]