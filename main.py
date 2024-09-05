from utils import Lexer, Parser

lexer = Lexer()
parser = Parser(lexer.tokenize('new a = "james is a boy";'))
parser = Parser(
    [["DECLARATION::new", "STR::VARIABLE::a", "ASSIGNMENT", "STR::'james'", "BREAK"]]
)
print(parser.parse())
