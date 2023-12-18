import numpy as np

from src.main.networks.sp_network import SPNetwork


class SPNetworkSFN(SPNetwork):

    def __init__(self, num_rounds, substitution_box, m):
        super().__init__(num_rounds)
        self.substitution_box = substitution_box
        self.m = m

    def round_function(self, value, constant):
        self.substitution(self.mix_rows(self.mix_columns(self.substitution(self.add_constant(value, constant)))))

    def inv_round_function(self, value, constant):
        self.substitution(self.mix_rows(self.mix_columns(self.substitution(self.add_constant(value, constant)))))

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
