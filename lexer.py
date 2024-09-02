'''
    GOAL:
        input : 1 + 1 * 5;
        output: [[INT::1, "PLUS", "INT::1", "MULTIPLY", "INT::5", "BREAK"]]
'''

class Lexer:
    def __init__(self):
        self.tokens = []
        self.token = []
        self.specials = ["+", "-", "*", "/", ";"]
        self.lastToken = ""
    def tokenize(self, ln):
        for n in range(len(ln)):
            i = ln[n]
            if i == " " and '"' not in self.lastToken and i not in self.specials:
                if self.lastToken != "":
                    self.token.append(self.lastToken)
                    self.lastToken = ""
            elif n+1 == len(ln) or n == len(ln):
                self.token.append(self.lastToken)
                self.lastToken = ""
                self.lastToken+= i
                self.token.append(self.lastToken)
                self.lastToken = ""
            elif i in self.specials:
                self.token.append(self.lastToken)
                self.lastToken = ""
                self.lastToken += i
                self.token.append(self.lastToken)
                self.lastToken = ""
            else:
                self.lastToken += i

        self.tokens.append(self.token)
        self.token = []
        self.lastToken = ""
        return self.tokens

lexer = Lexer()

print(lexer.tokenize("1 + 1;"))