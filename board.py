import math

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
                

        self.q1_prob = [[[1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
        self.q2_prob = self.q1_prob

    def step(self):
        for u in range(5):
            for v in range(5):
                self.q1_prob[u][v]
                

    def measure(self):
        #collapse wave function for position
        pass

    def apply_pauli_matrix(self, pauli_matrix):
        #apply pauli matrix to active qbit
        pass

    def propagate(self):
        