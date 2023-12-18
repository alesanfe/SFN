from src.main import matrix
from src.main.sfn import SFN


class PaperSFN(SFN):
    def __init__(self, num_rounds):
        super().__init__(num_rounds, matrix.sustitution_box1, matrix.sustitution_box2, matrix.permutation_box, matrix.xor_box, matrix.m)