import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_fromfile=pd.read_csv('kplr010666592-2011240104155_slc.csv')
print(df_fromfile.columns)
ax=df_fromfile['TIME']
ay=df_fromfile['PDCSAP_FLUX']
plt.plot(ax,ay)
plt.xlabel('TEMPO[s]')
plt.ylabel('FLUSSO[e-/s]')
plt.show()

plt.plot(ax,ay,'o-',color='limegreen')
plt.xlabel('TEMPO[s]')
plt.ylabel('FLUSSO[e-/s]')
plt.show()

plt.errorbar(ax,ay,yerr=df_fromfile['PDCSAP_FLUX_ERR'],fmt='o')
plt.xlabel('TEMPO[s]')
plt.ylabel('FLUSSO[e-/s]')
plt.show()

indice=ay.idxmin()
df2=df_fromfile.iloc[indice-5:indice+6]
fig, grafico = plt.subplots(figsize=(12,6))
grafico.errorbar(ax,ay,yerr=



    
            
