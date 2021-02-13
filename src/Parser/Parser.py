import re


class Parser:
    @staticmethod
    def match_in_string(str_: str = '', pattern: str = '') -> list:
        pattern_ = re.compile(pattern)
        span = [0, 0]
        matching_list = []

        while True:
            str_ = str_[span[1]:]
            matches = pattern_.search(str_)
            if matches == None:
                break
            matching_list.append(matches.group().strip())
            span = list(matches.span())

        return matching_list
