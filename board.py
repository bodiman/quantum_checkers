import math
import numpy as np

class Board():
    def __init__(self):
        self.active_qbit = None
        self.N = 10
        self.multiplier = [[0, 1, 4, 4, 1],
                                [1, 2, 5, 5, 2],
                                [4, 5, 8, 8, 5],
                                [4, 5, 8, 8, 5],
                                [1, 2, 5, 5, 2]]
        for i in range(5):
            for j in range(5):
                self.multiplier[i][j] = [math.cos(self.N / 2 * self.multiplier[i][j]), math.sin(self.N / 2 * self.multiplier[i][j])]

        self.q1_amplitude = [[[1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
        self.q2_amplitude = self.q1_amplitude

    def step(self):
        new_q1_amplitude = [[0] * 5] * 5
        new_q2_amplitude = [[0] * 5] * 5

        for y in range(5):
            for x in range(5):
                for v in range(5):
                    for u in range(5):
                        dx = (u - x + 5) % 5
                        dy = (v - y + 5) % 5
                        new_q1_amplitude[y][x][0] += self.q1_amplitude[v][u][0] * self.multiplier[dy][dx][0] - self.q1_amplitude[v][u][1] * self.multiplier[dy][dx][1]
                        new_q1_amplitude[y][x][1] += self.q1_amplitude[v][u][0] * self.multiplier[dy][dx][1] + self.q1_amplitude[v][u][1] * self.multiplier[dy][dx][0]
                        new_q2_amplitude[y][x][0] += self.q2_amplitude[v][u][0] * self.multiplier[dy][dx][0] - self.q2_amplitude[v][u][1] * self.multiplier[dy][dx][1]
                        new_q2_amplitude[y][x][1] += self.q2_amplitude[v][u][0] * self.multiplier[dy][dx][1] + self.q2_amplitude[v][u][1] * self.multiplier[dy][dx][0]

        self.q1_amplitude = new_q1_amplitude
        self.q2_amplitude = new_q2_amplitude

    def compute_normalization_factor(self, amplitude_matrix):
        total = 0

        for i in self.q1_amplitude:
            for j in i:
                total += j[0]**2 + j[1]**2

        return total

    def compute_prob(self, amplitude_matrix):
        normalization_factor = self.compute_normalization_factor(amplitude_matrix)

        prob = [[(j[0]**2 + j[1]**2)/normalization_factor for j in i] for i in self.q1_amplitude]

        return prob

    def measure(self, amplitude_matrix):
        prob_list = np.array(self.compute_prob(amplitude_matrix)).flatten()
        index = np.random.choice(len(prob_list), p=prob_list)
        y = index // 5
        x = index % 5

        amplitude_matrix = [[0, 0] * 5] * 5

        amplitude_matrix[y][x][0] = 1
        return amplitude_matrix

    def apply_pauli_matrix(self, pauli_matrix):
        #apply pauli matrix to active qbit
        pass