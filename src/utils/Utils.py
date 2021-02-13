import re


class Utils:

    @staticmethod
    def check_input(str_: str = '', reg: str = ''):
        if str_.count('=') != 1:
            print("Your input must have exactly one '=' sign")
            return False
        both_sides = str_.split(sep='=')
        for side in both_sides:
            if(not bool(re.match(reg, side))):
                print("This is not an equation !")
                return False
        return both_sides


    @staticmethod
    def switch_sign(items: list):
        for item in items:
            if list(item)[0] == '-':
                if list(item)[1] == 'X':
                    items[items.index(item)] = '+1 * ' + ''.join(list(item)[1:])
                else:
                    items[items.index(item)] = '+' + ''.join(list(item)[1:])
            elif item[0] == '+':
                if list(item)[1] == 'X':
                    items[items.index(item)] = '-1 * ' + ''.join(list(item)[1:])
                else:
                    items[items.index(item)] = '-' + ''.join(list(item)[1:])
            elif item[0].isnumeric():
                items[items.index(item)] = '-' + ''.join(item)
