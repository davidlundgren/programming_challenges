import fileinput
import operator


class Digit(object):
    TEMPLATE = (
                # 0
                (' - ',
                 '| |',
                 '   ',
                 '| |',
                 ' - '),
                # 1
                ('   ',
                 '  |',
                 '   ',
                 '  |',
                 '   '),
                # 2
                (' - ',
                 '  |',
                 ' - ',
                 '|  ',
                 ' - '),
                # 3
                (' - ',
                 '  |',
                 ' - ',
                 '  |',
                 ' - '),
                # 4
                ('   ',
                 '| |',
                 ' - ',
                 '  |',
                 '   '),
                # 5
                (' - ',
                 '|  ',
                 ' - ',
                 '  |',
                 ' - '),
                # 6
                (' - ',
                 '|  ',
                 ' - ',
                 '| |',
                 ' - '),
                # 7
                (' - ',
                 '  |',
                 '   ',
                 '  |',
                 '   '),
                # 8
                (' - ',
                 '| |',
                 ' - ',
                 '| |',
                 ' - '),
                # 9
                (' - ',
                 '| |',
                 ' - ',
                 '  |',
                 ' - '))

    def __init__(self, representation):
        self.representation = representation
    
    @classmethod
    def from_digit(cls, n, s):
        template = cls.TEMPLATE[int(n)]
        rows = [left + inner * s + right for left, inner, right in template]
        rows[1] = '\n'.join(rows[1] for _ in range(s))
        rows[3] = '\n'.join(rows[3] for _ in range(s))
        return cls('\n'.join(rows))

    def __str__(self):
        return self.representation

    def __add__(self, other):
        if not other:
            return self

        this_repr = str(self).split('\n')
        other_repr = str(other).split('\n')
        new_repr = []
        for row1, row2 in zip(this_repr, other_repr):
            new_repr.append(row1 + row2)
        return Digit('\n'.join(new_repr))


def lcd_digit(n, s):
    digits = [Digit.from_digit(digit, s) for digit in str(n)]
    return reduce(operator.add, digits)

if __name__ == '__main__':
    for line in fileinput.input():
        s, n = map(int, line.split())

        if not s and not n:
            break

        print str(lcd_digit(n, s) )
