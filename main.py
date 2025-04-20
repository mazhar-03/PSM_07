import numpy as np
import matplotlib.pyplot as plt

class PlateEquation:
    def __init__(self, size, top_temp, left_temp, bottom_temp, right_temp):
        self.n = size
        self.A = np.zeros((size * size, size * size))
        self.b = np.zeros(size * size)
        self.top = top_temp
        self.left = left_temp
        self.bottom = bottom_temp
        self.right = right_temp

    def build(self):
        idx = 0
        for i in range(self.n):
            for j in range(self.n):
                # Top
                if i == self.n - 1:
                    self.b[idx] += self.top
                else:
                    self.A[idx, (i + 1) * self.n + j] = 1
                # Bottom
                if i == 0:
                    self.b[idx] += self.bottom
                else:
                    self.A[idx, (i - 1) * self.n + j] = 1
                # Left
                if j == self.n - 1:
                    self.b[idx] += self.left
                else:
                    self.A[idx, i * self.n + j + 1] = 1
                # Right
                if j == 0:
                    self.b[idx] += self.right
                else:
                    self.A[idx, i * self.n + j - 1] = 1

                self.A[idx, idx] = -4
                idx += 1

    def get_matrix(self):
        return self.A

    def get_vector(self):
        return self.b


def gauss_solve(A, b):
    n = len(A)
    for i in range(n):
        max_row = i + np.argmax(np.abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


if __name__ == "__main__":
    size = 40
    top = 200
    left = 100
    bottom = 150
    right = 50

    eq = PlateEquation(size, top, left, bottom, right)
    eq.build()

    sol = gauss_solve(eq.get_matrix(), eq.get_vector())
    temp_map = sol.reshape(size, size)

    for i in range(size - 1, -1, -1):
        for j in range(size - 1, -1, -1):
            print(f"{sol[size * i + j]:.2f}", end=" ")
        print()

    plt.imshow(temp_map, cmap='inferno', origin='lower')
    plt.colorbar(label='Temperature')
    plt.title('Plate Temperature Distribution')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
