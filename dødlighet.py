import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

doed = pd.read_csv("https://www.uio.no/studier/emner/matnat/math/STK1100/data/doedelighet.txt",sep="\t")
alder= doed["alder"].values
menn = doed["menn"].values
kvinner = doed["kvinner"].values

# plt.semilogy(alder, menn, label="Menn")
# plt.semilogy(alder, kvinner, label="Kvinner")
# plt.xlabel("Alder")
# plt.ylabel("Dødssannsynlighet per 1000")
# plt.legend()
# plt.show()

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
# plt.step(alder, Fx_menn, where="post", label="Menn")
# plt.step(alder, Fx_kvinner, where="post", label="Kvinner")
# plt.xlabel("Alder")
# plt.ylabel("F(x)")
# plt.legend()
# plt.show()

# for år in [60, 70, 80, 90]:
#     print("Sannsynlighet for å bli " + str(år) + " år gammel:")
#     print("Menn: " + str((1 - Fx_menn[år])))
#     print("Kvinner: " + str((1 - Fx_kvinner[år])))

index = 0
for Fx in Fx_menn:
    if Fx >= 0.50:
        break
    index += 1
print("Medianalderen til menn er " + str(index) + " år")

index = 0
for Fx in Fx_kvinner:
    if Fx >= 0.50:
        break
    index += 1
print("Medianalderen til kvinner er " + str(index) + " år")

px_menn = []
for i in range(len(Fx_menn)):
    if i > 0:
        px_menn.append(Fx_menn[i] - Fx_menn[i-1])
    else:
        px_menn.append(Fx_menn[i])

px_kvinner = []
for i in range(len(Fx_kvinner)):
    if i > 0:
        px_kvinner.append(Fx_kvinner[i] - Fx_kvinner[i-1])
    else:
        px_kvinner.append(Fx_kvinner[i])

plt.plot(px_menn, label="Menn")
plt.plot(px_kvinner, label="Kvinner")
plt.xlabel("År")
plt.ylabel("Punksannsynlighet")
plt.grid()
plt.legend()
plt.show()

Ex_menn = 0
for i in range(len(px_menn)):
    alder = i
    px = px_menn[i]
    Ex_menn += alder * px
print(f"Forventet levealder for menn: {Ex_menn:.2f} år")

Ex_kvinner = 0
for i in range(len(px_kvinner)):
    alder = i
    px = px_kvinner[i]
    Ex_kvinner += alder * px
print(f"Forventet levealder for kvinner: {Ex_kvinner:.2f} år")

# Ser at medianen er høyere enn forventet levealder.

def h(X, a):
    if (X < a):
        return 0
    else:
        return X - a
    

print("Forventet gjenstående levealder for menn:")
for a in [30, 50, 80]:
    E_hx = 0
    for x in range(0, 107):
        E_hx += h(x, a) * px_menn[x]
    print(f"a={a}: {E_hx:.2f} år")

print("Forventet gjenstående levealder for kvinner:")
for a in [30, 50, 80]:
    E_hx = 0
    for x in range(0, 107):
        E_hx += h(x, a) * px_kvinner[x]
    print(f"a={a}: {E_hx:.2f} år")

E_hx_menn_liste = []
E_hx_kvinner_liste = []

for a in range(0, 107):
    E_hx_menn = 0
    E_hx_kvinner = 0
    for x in range(0, 107):
        E_hx_menn += h(x, a) * px_menn[x]
        E_hx_kvinner += h(x, a) * px_kvinner[x]
    E_hx_menn_liste.append(E_hx_menn)
    E_hx_kvinner_liste.append(E_hx_kvinner)

a = np.arange(0, 107)
plt.plot(a, E_hx_menn_liste, label="Menn")
plt.plot(a, E_hx_kvinner_liste, label="Kvinner")
plt.xlabel("Ved alder a")
plt.ylabel(f"Forventet gjenstående levealder")
plt.grid()
plt.legend()
plt.show()