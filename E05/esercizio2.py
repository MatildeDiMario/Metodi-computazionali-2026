import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import transforms
import scipy

sys.path.append('home/matilde/MCF/Metodi-computazionali-2026/E05')
sys.path
import randomwalk
x1,y1=randomwalk.randomwalk(1000,2)
x2,y2=randomwalk.randomwalk(1000,2)
x3,y3=randomwalk.randomwalk(1000,2)
x4,y4=randomwalk.randomwalk(1000,2)
x5,y5=randomwalk.randomwalk(1000,2)
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.show()
plt.savefig('randomwalker.png')

