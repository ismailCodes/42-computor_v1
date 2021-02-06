import re


class Parser:
    @staticmethod
    def match_in_string(str_: str = '', pattern: str = '') -> list:
        pattern_ = re.compile(pattern)
        span = [0, 0]
        matching_list = []
        i = 0
        while True:
            print(str_)
            str_ = str_[span[1]:]
            matches = pattern_.search(str_)
            if matches == None:
                break
            matching_list.append(matches.group().strip())
            span = list(matches.span())
            print(span)
            i += 1
            if i == 10:
                break
        return matching_list
