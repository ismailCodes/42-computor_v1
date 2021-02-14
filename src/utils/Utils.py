import re

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEAC = '\033[33m'

class Utils:

    @staticmethod
    def check_input(str_: str = '', reg: str = ''):
        if str_.count('=') != 1:
            print("Your input must have exactly one '=' sign")
            return False
        both_sides = str_.split(sep='=')
        for side in both_sides:
            if(not bool(re.match(reg, side))):
                print(f"Something went wrong here: {colors.FAIL}<< {side} >>{colors.DEAC}")
                return False
        return both_sides


    @staticmethod
    def switch_sign(items: list):
        for item in items:
            if item[0] == '-':
                if item[1] == 'X':
                    items[items.index(item)] = '+1 * ' + item[1:]
                else:
                    items[items.index(item)] = '+' + item[1:]
            elif item[0] == '+':
                if item[1] == 'X':
                    items[items.index(item)] = '-1 * ' + item[1:]
                else:
                    items[items.index(item)] = '-' + item[1:]
            elif item[0].isnumeric():
                items[items.index(item)] = '-' + item
