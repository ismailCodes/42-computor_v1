from Parser.Parser import Parser
from Utils.Utils import Utils
from Equation.Equation import Equation

test_str = "X^0  = - 5 * X^0 "
term_re = "(\\s*)([+-]?)(\\s*)(\\d*)(\.\\d+)?(\\s*)\*(\\s*)X(\\s*)\^(\\s*)\\d+(\\s*)"
equation_re = "(^(\s*([+-]?)\s*((\d*)(\.\d+)?\s*\*)?\s*X\^[012] *[+-]?)+$)"

both_sides = Utils.check_input(str_=test_str, reg=equation_re)
if both_sides:
    print(both_sides)
    left_side = Parser.match_in_string(both_sides[0], term_re)
    print(left_side)
    right_side = Parser.match_in_string(both_sides[1], term_re)
    Utils.switch_sign(right_side)
    print(right_side)
    equation_terms = left_side + right_side
    print(equation_terms)
    eq = Equation(equation_terms)
