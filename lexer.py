'''
    GOAL:
        input : 1 + 1 * 5;
        output: [[INT::1, "PLUS", "INT::1", "MULTIPLY", "INT::5", "BREAK"]]
        
'''

class Lexer:
    def __init__(self):
        self.tokens = []
        self.token = []
        self.tmpToken = []
        self.specials = ["+", "-", "*", "/", ";"]
        self.lastToken = ""
        self.keywords = {
            "new": "DECLARATION",
            "+": "PLUS",
            "-": "MINUS",
            "/": "DIVIDE",
            "*": "MULTIPLY"
        }
    def tokenize(self, ln):
        self.token = []
        self.tmpToken = []
        for n in range(len(ln)):
            i = ln[n]
            if i == " " and '"' not in self.lastToken and i not in self.specials:
                if self.lastToken != "":
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
            elif n+1 == len(ln) or n == len(ln):
                self.tmpToken.append(self.lastToken)
                self.lastToken = ""
                self.lastToken+= i
                self.tmpToken.append(self.lastToken)
                self.lastToken = ""
            elif i in self.specials:
                self.tmpToken.append(self.lastToken)
                self.lastToken = ""
                self.lastToken += i
                self.tmpToken.append(self.lastToken)
                self.lastToken = ""
            else:
                self.lastToken += i

        self.tokens.append(self.token)
        self.tmptoken = []
        self.lastToken = ""
        self.assignTypes(self.tmpToken)
        return self.tokens
    
    def assignTypes(self, token):
        self.lastToken = ""
        self.inString = False
        for n in range(len(token)):
            i = token[n]
            if self.inString:
                self.lastToken+= " "+i 
            else:
                self.lastToken+= i
            if i == "'" or i == '"' or "'" in i or '"' in i:
                if self.inString == True:
                    self.inString = False
                    self.token.append(self.lastToken)
                    self.lastToken = ""
                else:
                    self.inString = True
            elif self.inString == True:
                pass
            elif self.inString == False:
                self.token.append(self.lastToken)
                self.lastToken = ""
            elif i != "":
                self.token.append(self.lastToken)
                self.lastToken = ""
            else:
                pass
            

lexer = Lexer()

print(lexer.tokenize(input("Enter Code : ")))