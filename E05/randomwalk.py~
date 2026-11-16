import numpy as np
import sys
import matplotlib.pyplot as plt
import scipy
from matplotlib import transforms
sys.path.append('home/matilde/MCF/Metodi-computazionali-2026/E05')
sys.path
def randomwalk(n,s):
    angoli=np.random.uniform(low=0,high=2*np.pi, size=n)
    x=s*np.cos(angoli)
    y=s*np.sin(angoli)
    ax=np.array([0])
    ay=np.array([0])
    for i in range(len(x)): 
        ax=np.append(ax,x[i]+ax[i])
        ay=np.append(ay,y[i]+ay[i])
    return ax,ay



