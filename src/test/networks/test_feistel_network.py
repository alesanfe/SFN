import numpy as np
from src.main.networks.feistel_network import FeistelNetwork


class SampleFeistelNetwork(FeistelNetwork):
    def __init__(self, num_rounds):
        super().__init__(num_rounds)

    def round_function(self, plaintext, key):
        return plaintext + key


class TestFeistelNetwork:
    def test_encryption_decryption(self):
        key = [0b1100, 0b1010, 0b1111, 0b0101]
        num_rounds = 4
        feistel = SampleFeistelNetwork(num_rounds)

        plaintext = np.array([0b11011011, 0b01010101], dtype=np.uint8)

        ciphertext = feistel.encrypt(plaintext, key)
        decrypted_text = feistel.decrypt(ciphertext, key)

        assert np.array_equal(plaintext, decrypted_text)
