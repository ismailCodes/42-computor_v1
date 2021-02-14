import re
empty = [None, '']

class Parser:

    @staticmethod
    def match_in_string(str_: str = '', pattern: str = '') -> list:
        pattern_ = re.compile(pattern)
        span = [0, 0]
        res = {'0':[], '1':[], '2':[]}
        print(f'left side: {str_}')

        while True:
            str_ = str_[span[1]:]
            matches = pattern_.search(str_)
            if matches.group() in empty:
                break
            if matches.group('expo') in empty:
                
            print(f'coef: {matches.group("coef")}')
            print(f'expo: {matches.group("expo")}')
            # #     matching_list.append(matches.group())
            span = list(matches.span())
