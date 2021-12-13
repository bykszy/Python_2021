import numpy as np


def trim_matrix(bigger_matrix, row, col):
    del_row = np.delete(np.copy(bigger_matrix), row, 0)
    new = np.delete(del_row, col, 1)
    return new


def get_det(matrix):
    if len(matrix) == 1:
        return matrix[0, 0]
    else:
        det = 0
        for i in range(matrix.shape[1]):
            det += ((-1) ** i) * matrix[0, i] * get_det(trim_matrix(matrix, 0, i))
        return det


if __name__ == '__main__':
    dim = np.random.randint(1, 5)
    A = np.random.rand(dim, dim)
    print("Dimension of the matrix: ")
    print(dim)
    det_A = get_det(A)
    if np.allclose(det_A, np.linalg.det(A)):
        print("OK, result:")
        print(det_A)
    else:
        print("Something bad happened")
