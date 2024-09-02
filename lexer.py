'''
    GOAL:
        input : 1 + 1 * 5;
        output: [[INT::1, "PLUS", "INT::1", "MULTIPLY", "INT::5", "BREAK"]]
    
    BUGS:
        -cannot detect string

'''
import re

class Lexer:
    def __init__(self):
        self.tokens = []
        self.token = []
        self.tmpToken = []
        self.specials = ["+", "-", "*", "/", ";"]
        self.lastToken = ""
        self.chars = "abcdefghijklmnopqrstuvwxyz"
        self.nums = "1234567890"
        self.keywords = {
            "new": "DECLARATION",
            "func": "FUNCTION",
            "+": "PLUS",
            "-": "MINUS",
            "/": "DIVIDE",
            "*": "MULTIPLY",
            "=": "ASSIGNMENT",
            ";": "BREAK",
        }
    def tokenize(self, ln):
        self.token = []
        self.tmpToken = []
        for n in range(len(ln)):
            i = ln[n]
            i = i.replace('"', "'")
            if i == " " and i not in self.specials:
                if self.lastToken != "":
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
            elif n+1 == len(ln):
                if i == ";":
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
                    self.lastToken+= i
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
                else:
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
                if i == "'" or i == '"' or "'" in i or '"' in i:
                    self.inString = False
                    self.token.append(self.lastToken)
                    self.lastToken = ""
                else:
                    pass
            elif self.inString == False:
                self.token.append(self.lastToken)
                self.lastToken = ""
            elif i != "":
                self.token.append(self.lastToken)
                self.lastToken = ""
            else:
                pass
        for n in range(len(self.token)):
            i = self.token[n]
            if i in self.keywords:
                if i != "=" and i != ";":
                    self.token[n] = self.keywords[i] + "::" + i
                else:
                    self.token[n] = self.keywords[i]
                if i == "new":
                    if len(self.token) > n+1:
                        self.token[n+1] = "VARIABLE::"+self.token[n+1]
                        n+=1
                    else:
                        pass
            elif re.search(r"[0-9]",i):
                self.token[n] = "INT" + "::" + i
            elif re.search(r"[0-9a-zA-Z_-]", i):
                self.token[n] = "STR" + "::" + i
            else:
                pass

lexer = Lexer()

print(lexer.tokenize(input("Enter Code : ")))