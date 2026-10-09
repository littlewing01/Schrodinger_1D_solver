
#  Enter a potential V(x) dependent on x and find the energy eigenstates related to it by solving the Schrodinger equation.

What this code aims to do is take any input potential V(x) and then finds the corresponding eigenstates. We use basic linear algebra to solve Schrodinger equation numerically. We basically convert the differential equation to a matrix eigenvalue problem. 
The eigenvalues give us the energy of the state and the eigenvector is our wavefunction. 


## Understanding the code

Here are the main features of the code:

1. We create a hamiltonian matrix by essentially using the features of the tridiagonal matrix. Why would the hamiltonian be a tridiagonal matrix though?

This is because we just use the central finite difference approximation that helps convert a rather difficult differential equation computation to a matrix equation.
```python
  HamOP = diags(diagonals, [-1, 0, 1], format='csr')
  Hamiltonian = HamOP.toarray()
```

2. Now we find the eigenvalues of this matrix to find the energy eigenstates. 
```python
energy, psi = linalg.eigh(Hamiltonian)
```
And there we go, we get the main crux of our problem.

The solution is simple and elegant and requires a very basic understanding of calculus and quantum physics.
