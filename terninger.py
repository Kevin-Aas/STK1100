import numpy as np
import matplotlib.pyplot as plt

N = 500
T1 = np.random.randint(1, 7, N)
T2 = np.random.randint(1, 7, N)
X = T1 + T2

n = np.arange(1, N+1)
gjsnX = np.cumsum(X) / n

# plt.plot(n, gjsnX)
# plt.axis([0, N, 2, 12])
# plt.show()

Y = np.maximum(T1, T2)

n = np.arange(1, N+1)
gjsnY = np.cumsum(Y) / n

plt.plot(n, gjsnY)
plt.axis([0, N, 2, 12])
plt.show()

en = 0
to = 0
tre = 0
fire = 0
fem = 0
seks = 0
for y in Y:
    if y == 1:
        en += 1
    elif y == 2:
        to += 1
    elif y == 3:
        tre += 1
    elif y == 4:
        fire += 1
    elif y == 5:
        fem += 1
    elif y == 6:
        seks += 1
p_en = en/N
p_to = to/N
p_tre = tre/N
p_fire = fire/N
p_fem = fem/N
p_seks = seks/N

Ey = 1*p_en + 2*p_to + 3*p_tre + 4*p_fire + 5*p_fem + 6*p_seks
print(Ey)