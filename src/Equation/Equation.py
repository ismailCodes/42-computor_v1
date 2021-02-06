from Parser.Parser import Parser


class Term:
    def __init__(self, coefficient=0, exponent=0):
        self.coefficient = coefficient
        self.exponent = exponent


class Equation:
    def __init__(self, matching_list: list = []):
