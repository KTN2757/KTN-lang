class Token:
    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos


class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = {"+": "PLUS", "-": "MINUS", "*": "STAR",
                        "/": "SLASH", "(": "LPAREN", ")": "RPAREN"}
        self.tokens = []

    def run(self):
        self.tokenize()

    def tokenize(self):
        num_buf = ""
        num_start = 0
        for i in range(len(self.text)):
            if self.text[i] in self.DIGITS or self.text[i] == ".":
                if not num_buf:
                    num_start = i
                num_buf += self.text[i]

            else:
                if num_buf:
                    self.tokens.append(Token("NUMBER", num_buf, num_start))
                    num_buf = ""
                if self.text[i] in self.SYMBOLS:
                    self.tokens.append(
                        Token(self.SYMBOLS[self.text[i]], self.text[i], i))
            if self.text[i] == "\n":
                self.tokens.append(Token("END", self.text[i], i))

    def list_tokens(self):
        for i in self.tokens:
            print(f"Token[{i.pos}]: {i.type}({i.value})")


if __name__ == "__main__":
    with open("./ktn.ktn") as f:
        t = Tokenizer(f.read())
        t.run()
        t.list_tokens()
