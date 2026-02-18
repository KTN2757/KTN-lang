import string


class Token:
    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos


class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.DIGITS = string.digits
        self.SYMBOLS = {"+": "PLUS", "-": "MINUS", "*": "STAR",
                        "/": "SLASH", "(": "LPAREN", ")": "RPAREN", "=": "EQUAL"}
        self.LETTERS = string.ascii_letters
        self.tokens = []

    def run(self):
        self.tokenize()

    def tokenize(self):
        i = 0
        while i < len(self.text):
            i = self.next_token(i)

    def next_token(self, i):
        c = self.text[i]
        if c in self.DIGITS:
            return self.read_number(i)
        elif c in self.LETTERS:
            return self.read_var(i)
        elif c in self.SYMBOLS:
            self.tokens.append(Token(self.SYMBOLS[c], c, i))
        elif c == "\n":
            self.tokens.append(Token("END", c, i))
        elif c not in (" ", "\t"):
            self.tokens.append(Token("ILLEGAL", c, i))
        return i + 1

    def read_number(self, start):
        i = start
        while i < len(self.text) and (self.text[i] in self.DIGITS or (self.text[i] == "." and i > start)):
            i += 1
        self.tokens.append(Token("NUMBER", self.text[start:i], start))
        return i

    def read_var(self, start):
        i = start
        while i < len(self.text) and self.text[i] in self.LETTERS:
            i += 1
        self.tokens.append(Token("VAR", self.text[start:i], start))
        return i

    def list_tokens(self):
        for i in self.tokens:
            print(f"Token[{i.pos}]: {i.type}({i.value})")


if __name__ == "__main__":
    with open("./ktn.ktn") as f:
        t = Tokenizer(f.read())
        t.run()
        t.list_tokens()
