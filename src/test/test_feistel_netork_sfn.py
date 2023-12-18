import numpy as np
from src.main.feistel_network_sfn import FeistelNetworkSFN

class TestFeistelNetworkSFN:
    def test_encryption_decryption(self):
        substitution_box = np.array([0, 1, 3, 2], dtype=np.uint8)
        permutation_box = np.array([1, 0, 3, 2], dtype=np.uint8)
        xor_box = np.array([0, 1, 2, 3], dtype=np.uint8)
        num_rounds = 4
        feistel = FeistelNetworkSFN(num_rounds, substitution_box, permutation_box, xor_box)

        plaintext = np.array([0b11011011, 0b01010101], dtype=np.uint8)
        key = np.array([0b1100, 0b1010, 0b1111, 0b0101], dtype=np.uint8)

        ciphertext = feistel.encrypt(plaintext, key)
        decrypted_text = feistel.decrypt(ciphertext, key)

        assert np.array_equal(plaintext, decrypted_text)
