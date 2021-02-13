class Utils:
    @staticmethod
    def switch_sign(items: list):
        for item in items:
            if list(item)[0] == '-':
                items[items.index(item)] = '+' + ''.join(list(item)[1:])
            elif item[0] == '+':
                items[items.index(item)] = '-' + ''.join(list(item)[1:])
            elif item[0].isnumeric():
                items[items.index(item)] = '-' + ''.join(item)
