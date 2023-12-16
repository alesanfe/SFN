import numpy as np

from src.main.networks.feistel_network import FeistelNetwork
from src.main.networks.sp_network import SPNetwork


class SFN:

    def __init__(self,num_rounds, substitution_box1, substitution_box2, permutation_box, xor_box, m):
        self.num_rounds = num_rounds
        self.substitution_box1 = substitution_box1
        self.substitution_box2 = substitution_box2
        self.permutation_box = permutation_box
        self.xor_box = xor_box
        self.m = m

    def encrypt_all(self, plaintext, keys):
        iterations = len(plaintext) // 64
        ciphertext = []
        for i in range(iterations):
            state = []
            for j in range(8):
                row = []
                for k in range(8):
                    row.append(plaintext[i*8+j*8+k])
                state.append(row)
            state = np.array(state)
            ciphertext.append(self.encrypt(state, keys[iterations]))

    def decrypt_all(self, ciphertext, keys):
        iterations = len(ciphertext) // 64
        plaintext = []
        for i in range(iterations):
            state = []
            for j in range(8):
                row = []
                for k in range(8):
                    row.append(ciphertext[i*8+j*8+k])
                state.append(row)
            state = np.array(state)
            plaintext.append(self.decrypt(state, keys[iterations]))
    def encrypt(self, state, key):

        rk = key[:63]
        ck = key[64:]
        self.rks = [rk]
        for i in range(len(ck)):
            signal = ck[i]
            state = self.ecnryptation_and_decryption(signal, state, rk)
            rk = self.expansion_key(signal, rk, i)
            self.rks.append(rk)
        left, right = np.split(state, 2)
        state = np.concatenate((right, left))
        state = self.add_round_key(state, rk)
        return state

    def decrypt(self, state, key):
        rk = key[:63]
        ck = key[64:]
        for i in range(len(ck)-1, -1, -1):
            signal = ck[i]
            state = self.ecnryptation_and_decryption(signal, state, self.rks[i]) # TODO: No tiene sentido que sea tan fácil desencriptar.
        left, right = np.split(state, 2)
        state = np.concatenate((right, left))
        state = self.add_round_key(state, rk)
        return state


    def add_round_key(self, state, rk):
        return np.bitwise_xor(state, rk)


    def ecnryptation_and_decryption(self, signal, state, rk):
        if signal == 0:
            sp = SPNetwork(1, self.substitution_box1, self.m)
            state = sp.encrypt(state, rk)

        else:
            feistel =  FeistelNetwork(1, self.substitution_box2, self.permutation_box, self.xor_box)
            state = feistel.encrypt(state, rk)
        return state

    def expansion_key(self, signal, rk, i):
        if signal == 0:
            feistel = FeistelNetwork(1, self.substitution_box1, self.permutation_box, self.xor_box)
            rk = feistel.encrypt(rk, i)

        else:
            sp = SPNetwork(1, self.substitution_box2, self.m)
            rk = rk.encrypt(rk, i)
        return rk
