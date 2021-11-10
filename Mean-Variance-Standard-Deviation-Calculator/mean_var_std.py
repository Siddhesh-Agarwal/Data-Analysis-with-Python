import numpy as np

def calculate(arr):
    if len(arr) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix1 = np.array(arr)
    matrix2 = matrix1.reshape(3, 3)
    calculations = {"mean": [list(np.mean(matrix2, axis=0)), list(np.mean(matrix2, axis=1)), np.mean(matrix1)],
                    "variance": [list(np.var(matrix2, axis=0)), list(np.var(matrix2, axis=1)), np.var(matrix1)],
                    "standard deviation": [list(np.std(matrix2, axis=0)), list(np.std(matrix2, axis=1)), np.std(matrix1)],
                    "max": [list(np.max(matrix2, axis=0)), list(np.max(matrix2, axis=1)), np.max(matrix1)],
                    "min": [list(np.min(matrix2, axis=0)), list(np.min(matrix2, axis=1)), np.min(matrix1)],
                    "sum": [list(np.sum(matrix2, axis=0)), list(np.sum(matrix2, axis=1)), np.sum(matrix1)]
    }
    return calculations
