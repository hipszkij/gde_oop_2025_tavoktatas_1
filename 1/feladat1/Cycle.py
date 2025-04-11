import math


def korKerulet(r):
    return 2 * r * math.pi


def korTerulet(r):
    return math.pow(r, 2) * math.pi


r = 4;

print(korKerulet(r))
print(korTerulet(r))
