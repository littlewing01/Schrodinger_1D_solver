
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from scipy.linalg import eigh
from scipy.sparse import diags


hbar = 1.055e-34
m = 9.1e-31


N = 200

L = 1e-9
dx = L / (N + 1)
x = np.linspace(dx, L - dx, N)


def V(x):
    symx = sp.symbols('x')
    user_expr = input("Potential expression to be entered: ")
    expression = parse_expr(user_expr)
    f = sp.lambdify(symx, expression, 'numpy')
    return f(x)

v = V(x)

# Hamiltonian matrix
f1 = -hbar**2 / (2 * m * dx**2)
f2 = hbar**2 / (m * dx**2) + v

diagonals = [
    np.full(N - 1, f1),
    f2,
    np.full(N - 1, f1)
]

Hamiltonian = diags(
    diagonals, [-1, 0, 1], format='csr'
).toarray()

# Solve the eigenvalue problem
energy, psi = eigh(Hamiltonian)

print("First five allowed energy states (J):")
print(energy[:5])

print("First five allowed energy states (eV):")
print(energy[:5] / 1.602176634e-19)

# Plot the first five eigenfunctions
for i in range(5):
    plt.plot(x, psi[:, i], label=f"State {i}")

plt.xlabel("Position x (m)")
plt.ylabel("Wavefunction (arbitrary scale)")
plt.title("First five energy eigenstates")
plt.legend()
plt.tight_layout()
plt.show()