from re import split
from Parser.Parser import Parser


class Term:
    def __init__(self, coefficient=0, exponent=0):
        self.coefficient = coefficient
        self.exponent = exponent


class Equation:

    @staticmethod
    def is_digit(n):
        try:
            int(n)
            return True
        except ValueError:
            return  False

    @staticmethod
    def fill_terms(terms_list: list):
        ret_terms = []
        for term in terms_list:
            split_terms = term.split('*')
            split_terms = [x.strip().replace(' ', '') for x in x]
            if len(split_terms) == 1:
                if Equation.is_digit(split_terms[0]):
                    t = Term(coefficient=split_terms[0])
                elif split_terms[0][0] == 'X':
                    exponent = split_terms[0].split('^')[1]
                    t = Term(exponent=exponent)


    def __init__(self, matching_list: list = []):
        self.terms = Equation.fill_terms(matching_list)
