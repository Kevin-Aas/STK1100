import numpy as np
import math

alpha = np.arange(0, 12)
perioder = np.array([57,
           203,
           383,
           525,
           532,
           408,
           273,
           139,
           45,
           27,
           10,
           6])

ant_perioder = sum(perioder)
ant_partikler = 0
for i in range(0, 12):
    ant_partikler += i * perioder[i]

snitt = ant_partikler / ant_perioder
print("Gjennomsnittlig antall partikler per periode:")
print(round(snitt, 3))

lmda = snitt
# Poisson fordeling med parameter lmda:
poisson = []
for x in range(0, 12):
    px = np.exp(-lmda) * lmda**(x) / math.factorial(x)
    poisson.append(px)

import matplotlib.pyplot as plt
plt.plot(alpha, perioder/ant_perioder, label="Data")
plt.plot(alpha, poisson, "--", label="Poisson")
plt.xlabel("Antall partikler")
plt.ylabel("Frekvens")
plt.title("Data sammenlignet med Poisson-modell")
plt.grid()
plt.legend()
plt.show()