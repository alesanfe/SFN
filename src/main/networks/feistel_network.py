from operator import xor
import numpy as np

import numpy as np

class FeistelNetwork:

    def __init__(self, num_rounds, round_function, substitution_box, permutation_box, xor_box):
        self.num_rounds = num_rounds
        self.round_function = round_function
        self.substitution_box = substitution_box
        self.permutation_box = permutation_box
        self.xor_box = xor_box

    def encrypt(self, plaintext, key):
        left, right = np.split(plaintext, 2)

        for i in range(self.num_rounds):
            left, right = right, np.bitwise_xor(left, self.round_function(right, key[i]))

        return np.concatenate((left, right))

    def decrypt(self, ciphertext, key):
        left, right = np.split(ciphertext, 2)

        for i in range(self.num_rounds - 1, -1, -1):
            left, right = np.bitwise_xor(right, self.round_function(left, key[i])), left

        return np.concatenate((left, right))

    def round_function(self, value, constant):
        return self.add_constant(self.substitution(self.permutation(self.mix_xor(value))), constant)

    def add_constant(self, value, constant):
        return np.bitwise_xor(value, constant)

    def substitution(self, value):
        result = np.zeros_like(value)
        for i in range(len(value)):
            result[i] = self.substitution_box[value[i]]
        return result

    def permutation(self, value):
        result = np.zeros_like(value)
        for i in range(len(value)):
            result[i] = self.permutation_box[value[i]]
        return result

    def mix_xor(self, value):
        result = value[self.xor_box[0]]
        for i in range(1, len(self.xor_box)):
            result = np.bitwise_xor(result, value[self.xor_box[i]])
        return result

