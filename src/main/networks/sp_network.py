import numpy as np

class SPNetwork:
    def __init__(self, num_rounds, substitution_box, m):
        self.num_rounds = num_rounds
        self.substitution_box = substitution_box
        self.m = m

    def encrypt(self, plaintext, key):
        value = plaintext.copy()
        for i in range(self.num_rounds):
            left, right = np.split(value, 2)
            value = np.concatenate((right, left))
            value = self.round_function(value, key[i])
        return value

    def decrypt(self, ciphertext, key):
        value = ciphertext.copy()
        for i in range(self.num_rounds - 1, -1, -1):
            left, right = np.split(value, 2)
            value = np.concatenate((right, left))
            value = self.round_function(value, key[i])
        return value

    def round_function(self, value, constant):
        return self.add_constant(self.substitution(self.mix_columns(self.mix_rows(self.substitution(value)))), constant)

    def add_constant(self, value, constant):
        return np.bitwise_xor(value, constant)

    def substitution(self, value):
        result = np.zeros_like(value)
        for i in range(len(value)):
            result[i] = self.substitution_box[value[i]]
        return result

    def mix_columns(self, value):
        return np.dot(self.m, value.T).T

    def mix_rows(self, value):
        return np.dot(value.T, self.m).T
