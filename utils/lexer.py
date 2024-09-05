'''
    GOAL:
        input : 1 + 1 * 5;
        output: [[INT::1, "PLUS", "INT::1", "MULTIPLY", "INT::5", "BREAK"]]
    
    BUGS:
        - line does not need to end with ; when assigning string variables
        - need to work for one word strings e.g "life"
        - switch to re.search() to find strings and other variable types
        - add more keywords
        - find bugs
        - might rewrite lexer (most likely)
        - can't detect floats :/
        - can't tokenize without using ; at the end
        - if new; is typed it tokenizes and invisible variable name e.g [['DECLARATION', 'STR::VARIABLE::', 'BREAK']]
        - cannot detect keywords if ; is not use to end e.g new -> [['STR::n', 'STR::w']]
        - cannot detect strings when only typed e.g input -> "a"
'''
import re
from .vars import LEX_KEYWORDS

class Lexer:
    def __init__(self):
        self.tokens = []
        self.token = []
        self.tmpToken = []
        self.specials = ["+", "-", "*", "/", ";", "new"]
        self.lastToken = ""
        self.chars = "abcdefghijklmnopqrstuvwxyz"
        self.nums = "1234567890"
        self.keywords = LEX_KEYWORDS
        
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
            elif n + 1 == len(ln):
                if i == ";":
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
                    self.lastToken += i
                    self.tmpToken.append(self.lastToken)
                    self.lastToken = ""
                else:
                    self.lastToken += i
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
        self.inString = 1
        for n in range(len(token)):
            i = token[n]
            self.lastToken += i
            if i != "" and ("'" not in i and '"' not in i) and (self.inString % 2) == 1:
                self.token.append(self.lastToken)
                self.lastToken = ""
            elif  i != "" and ("'" not in i and '"' not in i) and (self.inString % 2) == 0:
                self.lastToken += " "
            elif i != "" and ("'" in i or '"' in i):
                self.inString += 1
                self.lastToken += " "
        self.lastToken = self.token[len(self.token)-1]
        self.token.pop()
        self.tmpToken = self.lastToken[(len(self.lastToken)-1):]
        self.lastToken = self.lastToken[:(len(self.lastToken)-2)]
        self.token.append(self.lastToken)
        self.token.append(self.tmpToken)
        for n in range(len(self.token)):
            i = self.token[n]
            if i in self.keywords:
                if i != "=" and i != ";":
                    self.token[n] = self.keywords[i]
                else:
                    self.token[n] = self.keywords[i]
                if i == "new":
                    if len(self.token) > n + 1:
                        self.token[n + 1] = "VARIABLE::" + self.token[n + 1]
                        n += 1
                    else:
                        pass
            elif re.search(r"[0-9]", i):
                self.token[n] = "INT" + "::" + i
            elif re.search(r"[0-9.]",i):
                self.token[n] = "FLT" + "::" + i
            elif re.search(r"[0-9a-zA-Z_-]", i):
                self.token[n] = "STR" + "::" + i
            else:
                pass


lexer = Lexer()
# print(lexer.tokenize(input("Enter Code : ")))
# print(lexer.tokenize('new a = "james";'))

#print(lexer.tokenize(input("Enter Code : ")))
print(lexer.tokenize(input("Enter Code : ")))