from utils import Lexer, Parser
from __init__ import VERSION

lexer = Lexer()
#parser = Parser(
#    [["DECLARATION::new", "STR::VARIABLE::a", "ASSIGNMENT", "INT::5",  "BREAK"]]
#)
parser = Parser(lexer.tokenize(input("bind "+VERSION+" > ")))
print(parser.parse())