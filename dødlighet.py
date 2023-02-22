import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

doed = pd.read_csv("https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedelighet.txt",sep="\t")
alder= doed["alder"].values
menn = doed["menn"].values
kvinner = doed["kvinner"].values

plt.semilogy(alder, menn, label="Menn")
plt.semilogy(alder, kvinner, label="Kvinner")
plt.xlabel("Alder")
plt.ylabel("Dødssannsynlighet per 1000")
plt.legend()
plt.show()

# Kommentar til plottet:
'''
Vi ser klart at det er større dødlighet hos menn enn hos kvinner ved første øyekast.
Dødligheten hos menn er markant større enn hos kvinnene 20 årene, som mest sannsynlig
skyldes av at mange unge menn havner i bilulykker sammenliknet med kvinner på samme
alder. Generelt sett kan man si at det er større sannsynlighet for at menn dør enn
kvinner.
'''

qx_menn = menn/1000
qx_kvinner = kvinner/1000

Sx_menn = np.cumprod(1 - qx_menn)
Sx_kvinner = np.cumprod(1 - qx_kvinner)
Fx_menn = 1 - Sx_menn
Fx_kvinner = 1 - Sx_kvinner
plt.step(alder, Fx_menn, where="post", label="Menn")
plt.step(alder, Fx_kvinner, where="post", label="Kvinner")
plt.xlabel("Alder")
plt.ylabel("F(x)")
plt.legend()
plt.show()

for år in [60, 70, 80, 90]:
    print("Sannsynlighet for å bli " + str(år) + " år gammel:")
    print("Menn: " + str((1 - Fx_menn[år])))
    print("Kvinner: " + str((1 - Fx_kvinner[år])))

