import numpy as np

class FeistelNetwork:

    def __init__(self, num_rounds):
        self.num_rounds = num_rounds

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
        pass

