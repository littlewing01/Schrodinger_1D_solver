import scipy as sc
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy import linalg
from scipy.sparse import diags

#Making the constants
hbar=1.05*10**(-34)
m=9.1*10**(-31)
w=10**12

def square(x):
    return x**2

x=np.array([1,2,3,4,5])
print(square(x)+2)


from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr



def V(x):
    symx= symbols('x')
    user_expr = input("potential expression to be entered")
    expression = parse_expr(user_expr)
    f = sp.lambdify(symx, expression, 'numpy')
    return f(x)


N=200

x, delta_x=np.linspace(0,1,N,retstep=True)
v=V(x)

f_1= -hbar**2 / (2*m*delta_x**2)
f_2=hbar**2 / (m*delta_x**2) + v

diag1=np.array(f_2)
diag2=np.full(N-1, f_1)

diagonals = [diag2, diag1, diag2]

HamOP = diags(diagonals, [-1, 0, 1], format='csr')
Hamiltonian = HamOP.toarray()
energy, psi = linalg.eigh(Hamiltonian)


print("Allowed energy states are", energy)


