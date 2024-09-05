from utils import Lexer, Parser
from __init__ import VERSION

lexer = Lexer()
parser = Parser(lexer.tokenize(input("bind "+VERSION+" > ")))
#parser = Parser(
#    [["DECLARATION::new", "STR::VARIABLE::a", "ASSIGNMENT", "STR::'james'", "BREAK"]]
#)
print(parser.parse())