import numpy as np

from src.main.networks.sp_network import SPNetwork


class SampleSPNetwork(SPNetwork):
    def __init__(self, num_rounds):
        super().__init__(num_rounds)

    def round_function(self, value, constant):
        return value + constant

    def inv_round_function(self, value, constant):
        return value - constant

class TestSPlNetwork:
    def test_encryption_decryption(self):
        key = [0b1100, 0b1010, 0b1111, 0b0101]
        num_rounds = 4
        sp = SampleSPNetwork(num_rounds)

        plaintext = np.array([0b11011011, 0b01010101], dtype=np.uint8)

        ciphertext = sp.encrypt(plaintext, key)
        decrypted_text = sp.decrypt(ciphertext, key)

        print(plaintext)
        print(ciphertext)
        print(decrypted_text)

        assert np.array_equal(plaintext, decrypted_text)