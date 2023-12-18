import numpy as np

from src.main.networks.feistel_network import FeistelNetwork


class FeistelNetworkSFN(FeistelNetwork):
    def __init__(self, num_rounds, substitution_box, permutation_box, xor_box):
        super().__init__(num_rounds)
        self.substitution_box = substitution_box
        self.permutation_box = permutation_box
        self.xor_box = xor_box

    def round_function(self, value, constant):
        return self.mix_xor(self.permutation(self.substitution(self.add_constant(value, constant))))

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
