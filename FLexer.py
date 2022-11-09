from sly import Lexer


class FLexer(Lexer):
    tokens = {INTEGER, STRING}

    INTEGER = r'\d+'
    STRING = r'"[^"]*"'

    ignore = r' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'\#.*'

    literals = {"(", ")", "S", "G", "L"}


