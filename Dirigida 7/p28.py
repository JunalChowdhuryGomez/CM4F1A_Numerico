import numpy as np
A = np.array([[3, 2, 1], 
              [2, 3, 2], 
              [1, 2, 3]]),

B = np.array([[4, 3, 2, 1], 
              [3, 4, 3, 2], 
              [2, 3, 4, 3], 
              [1, 2, 3, 4]]),

C = np.array([[2.75, -0.25, -0.75, 1.25], 
              [-0.25, 2.75, 1.25, -0.75], 
              [-0.75, 1.25, 2.75, -0.25], 
              [1.25, -0.75, -0.25, 2.75]]),

D = np.array([[3.6, 4.4, 0.8, -1.6, -2.8], 
              [4.4, 2.6, 1.2, -0.4, 0.8], 
              [0.8, 1.2, 0.8, -4.0, -2.8], 
              [-1.6, -0.4, -4.0, 1.2, 2.0], 
              [-2.8, 0.8, -2.8, 2.0, 1.8]])

print(F"Matriz A = {A} \n valores propios: {np.linalg.eigvals(A)} \n ---------------------")
print(F"Matriz B = {B} \n valores propios: {np.linalg.eigvals(B)} \n ---------------------")
print(F"Matriz C = {C} \n valores propios: {np.linalg.eigvals(C)} \n ---------------------")
print(F"Matriz D = {D} \n valores propios: {np.linalg.eigvals(D)} \n ---------------------")
