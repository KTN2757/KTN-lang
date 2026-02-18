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
        num_buf = ""
        letter_buf = ""
        num_start = 0
        letter_start = 0
        for i in range(len(self.text)):
            if self.text[i] in self.DIGITS or (self.text[i] == "." and num_buf):
                if letter_buf:
                    self.tokens.append(Token("VAR", letter_buf, letter_start))
                    letter_buf = ""
                if not num_buf:
                    num_start = i
                num_buf += self.text[i]

            elif self.text[i] in self.LETTERS:
                if num_buf:
                    self.tokens.append(Token("NUMBER", num_buf, num_start))
                    num_buf = ""
                if not letter_buf:
                    letter_start = i
                letter_buf += self.text[i]

            else:
                if num_buf:
                    self.tokens.append(Token("NUMBER", num_buf, num_start))
                    num_buf = ""
                if letter_buf:
                    self.tokens.append(Token("VAR", letter_buf, letter_start))
                    letter_buf = ""
                if self.text[i] in self.SYMBOLS:
                    self.tokens.append(
                        Token(self.SYMBOLS[self.text[i]], self.text[i], i))
                elif self.text[i] not in (" ", "\t", "\n"):
                    self.tokens.append(Token("ILLEGAL", self.text[i], i))

            if self.text[i] == "\n":
                self.tokens.append(Token("END", self.text[i], i))

        if num_buf:
            self.tokens.append(Token("NUMBER", num_buf, num_start))
        if letter_buf:
            self.tokens.append(Token("VAR", letter_buf, letter_start))

    def list_tokens(self):
        for i in self.tokens:
            print(f"Token[{i.pos}]: {i.type}({i.value})")


if __name__ == "__main__":
    with open("./ktn.ktn") as f:
        t = Tokenizer(f.read())
        t.run()
        t.list_tokens()
