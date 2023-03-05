import math

print("Antar binomisk fordeling med p=0.5:")
print(" x  |  p(x) [%]    ")
print("----+-----------")
for x in range(0, 12+1):
    kombinasjoner = math.factorial(12) / (math.factorial(12-x) * math.factorial(x))
    gutter = 0.5**(x)
    jenter = 0.5**(12-x)
    p_x = kombinasjoner * gutter * jenter
    if x < 10:
        print(f" {x}  |  {p_x*100:.2f}")
    else:
        print(f" {x} |  {p_x*100:.2f}")

print("\nFra data:")
antall_familier = [3, 24, 104, 286, 670, 1033, 1343, 1112, 829, 478, 181, 45, 7]
print(" x  |  p(x) [%]    ")
print("----+-----------")
antall_gutter = 0
antall_jenter = 0
for x in range(0, 12+1):
    antall_gutter += antall_familier[x] * x
    antall_jenter += antall_familier[x] * (12 - x)
    p_x = antall_familier[x] / 6115
    if x < 10:
        print(f" {x}  |  {p_x*100:.2f}")
    else:
        print(f" {x} |  {p_x*100:.2f}")
antall_barn = antall_gutter + antall_jenter
print("Gutter:")
print(f"- Antall: {antall_gutter}")
print(f"- Relativ frekvens = {antall_gutter / antall_barn:.2f}")
print("Jenter:")
print(f"- Antall: {antall_jenter}")
print(f"- Relativ frekvens = {antall_jenter / antall_barn:.2f}\n")

print("Antar binomisk fordeling med p=0.52:")
print(" x  |  p(x) [%]    ")
print("----+-----------")
for x in range(0, 12+1):
    kombinasjoner = math.factorial(12) / (math.factorial(12-x) * math.factorial(x))
    gutter = 0.52**(x)
    jenter = 0.48**(12-x)
    p_x = kombinasjoner * gutter * jenter
    if x < 10:
        print(f" {x}  |  {p_x*100:.2f}")
    else:
        print(f" {x} |  {p_x*100:.2f}")