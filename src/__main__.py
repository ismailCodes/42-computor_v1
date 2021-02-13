from Parser.Parser import Parser
from Utils.Utils import Utils
from Equation.Equation import Equation

test_str = "- 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 - 5 * X^0 + 4 * X^1 - 9.3 * X^14 - 5 * X^0"
term_re = "(\\s*)([+-]?)(\\s*)(\\d*)(\.\\d+)?(\\s*)\*(\\s*)X(\\s*)\^(\\s*)\\d+(\\s*)"

n = test_str.split(sep='=')
left_side = Parser.match_in_string(n[0], term_re)
right_side = Parser.match_in_string(n[1], term_re)
Utils.switch_sign(right_side)
equation_terms = left_side + right_side
eq = Equation(equation_terms)
