import numpy as np

class SPNetwork:
    def __init__(self, num_rounds):
        self.num_rounds = num_rounds

    def encrypt(self, plaintext, key):
        value = plaintext.copy()
        for i in range(self.num_rounds):
            left, right = np.split(value, 2)
            print(value)
            value = np.concatenate((right, left))
            print(value)
            value = self.round_function(value, key[i])
        return value

    def decrypt(self, ciphertext, key):
        value = ciphertext.copy()
        for i in range(self.num_rounds):
            left, right = np.split(value, 2)
            value = np.concatenate((right, left))
            value = self.inv_round_function(value, key[i])
        return value

    def round_function(self, value, constant):
        pass

    def inv_round_function(self, value, constant):
        pass