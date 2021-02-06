from Parser.Parser import Parser

test_str = "- 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 - 5 * X^0 + 4 * X^1 - 9.3 * X^14"
term_re = "(\\s*)([+-]?)(\\s*)(\\d*)(\.\\d+)?(\\s*)\*(\\s*)X(\\s*)\^(\\s*)\\d+(\\s*)"

n = test_str.split(sep='=')
print(type(n[0]), type(n[1]))
left_side = Parser.match_in_string(n[0])
# right_side = Parser.match_in_string(n[1])
# print(left_side, right_side)
