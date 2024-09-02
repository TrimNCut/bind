'''
    GOAL:
        input : 1 + 1 * 5;
        output: [[INT::1, "PLUS", "INT::1", "MULTIPLY", "INT::5", "BREAK"]]
'''

class Lexer:
    def __init__(self):
        self.tokens = []
        self.token = []
        self.specials = ["+", "-", "*", "/"]
        self.lastToken = ""
    def tokenize(self, ln):
        for i in ln:
            if i == " ":
                self.token.append(self.lastToken)
                self.lastToken = ""
            else:
                self.lastToken += i

        return self.token

lexer = Lexer()

print(lexer.tokenize("1 + 1 = 5;"))