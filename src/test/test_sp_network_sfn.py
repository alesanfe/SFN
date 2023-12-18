import numpy as np

from src.main.sp_network_sfn import SPNetworkSFN


class TestSPNetworkSFN:
    def test_encryption_decryption(self):
        substitution_box = np.array([0, 1, 3, 2], dtype=np.uint8)
        m = np.array([1, 0, 3, 2], dtype=np.uint8)
        num_rounds = 4
        feistel = SPNetworkSFN(num_rounds, substitution_box, m)

        plaintext = np.array([0b11011011, 0b01010101], dtype=np.uint8)
        key = np.array([0b1100, 0b1010, 0b1111, 0b0101], dtype=np.uint8)

        ciphertext = feistel.encrypt(plaintext, key)
        decrypted_text = feistel.decrypt(ciphertext, key)

        assert np.array_equal(plaintext, decrypted_text)