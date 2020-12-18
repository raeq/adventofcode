from itertools import tee

from more_itertools import unzip
from sly import Lexer, Parser


class MathLexer(Lexer):
    tokens = {NUMBER}
    ignore = ' '
    literals = {'+', '*', '(', ')'}

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t


class MathParser(Parser):
    tokens = MathLexer.tokens

    precedence = (
        ('left', '+', '*'),
        ('left', '(', ')'),
    )

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER


class AdvancedMathParser(MathParser):
    tokens = MathLexer.tokens

    precedence = (
        ('left', '*'),
        ('left', '+'),
        ('left', '(', ')'),
    )

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('"(" expr ")"')
    def expr(self, p):
        return p.expr

    @_('expr "+" expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr "*" expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('NUMBER')
    def expr(self, p):
        return p.NUMBER


def load_file(file_name: str) -> list:
    with open(file_name, 'r') as fd:
        return [_.strip() for _ in fd.readlines()]


def part_one(tokens_a):
    parser = MathParser()
    return sum(map(parser.parse, tokens_a))


def part_two(tokens_b):
    parser = AdvancedMathParser()
    return sum(map(parser.parse, tokens_b))


def main():
    data = load_file("day18.txt")

    lexer = MathLexer()
    tokens_a, tokens_b = unzip(tee(lexer.tokenize(line)) for line in data)

    print(f" Part one solution: {part_one(tokens_a):>16}")
    print(f" Part two solution: {part_two(tokens_b):>16}")


if __name__ == '__main__':
    main()
