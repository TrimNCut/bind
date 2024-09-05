from utils import Lexer, Parser

lexer = Lexer()
parser = Parser(lexer.tokenize('new a = "james"'))
parser.parse()
