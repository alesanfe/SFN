import numpy as np
from src.main.paper_sfn import PaperSFN

class TestSFN:
    def test_encryption_decryption(self):
        num_rounds = 4
        sfn = PaperSFN(num_rounds)

        plaintext = np.array([0b11011011, 0b01010101, 0b11011011, 0b01010101], dtype=np.uint8) # TODO: Poner datos válidos.
        keys = np.array([0b11001100, 0b10101010, 0b11111111, 0b01010101], dtype=np.uint8) # TODO: Poner datos válidos.

        ciphertext = sfn.encrypt_all(plaintext, keys)
        decrypted_text = sfn.decrypt_all(ciphertext, keys)

        assert np.array_equal(plaintext, decrypted_text)
