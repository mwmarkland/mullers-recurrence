# Muller's Recurrence
# Code from the website:
# https://scipython.com/blog/mullers-recurrence

# Want to tweak and experiment, but this is the start.

import numpy as np
from fractions import Fraction

def E_float(y, z):
    """Naive implementation of Muller's recurrence."""
    return 108 - (815 - 1500 / z) / y

def E_float2(y, _):
    """Numerically stable implementation of Muller's recurrence."""
    return 8 - 15/y

def E_fraction(y, z):
    """Muller's recurrence implemented with rational arithmetic."""
    return 108 - Fraction((815 - Fraction(1500, z)), y)

def do_recurrence(E, x):
    for n in range(2, N+1):
        x[n] = E(x[n-1], x[n-2])

N = 80
x_fraction = [0]*(N+1)
x_fraction[0], x_fraction[1] = 4, Fraction(17, 4)
do_recurrence(E_fraction, x_fraction)

x_float = [0]*(N+1)
x_float[0], x_float[1] = 4, 4.25
do_recurrence(E_float, x_float)

x_float2 = [0]*(N+1)
x_float2[0], x_float2[1] = 4, 4.25
do_recurrence(E_float2, x_float2)

print(' n {:>22s} {:^22s} {:^22s}'.format('rational arithmetic',
                    'floating point 1', 'floating point 2'))
print('--', '-'*22, '-'*22, '-'*22)
for n in range(N+1):
    print('{:2d} {:22.15f} {:22.15f} {:22.15f}'.format(n, float(x_fraction[n]),
                                             x_float[n], x_float2[n]))
