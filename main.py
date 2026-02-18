class Token:
    def __init__(self, type, value, pos):
        self.type = type  # Symbol or Number or END
        self.value = value
        self.pos = pos


class Tokenizer:
    def __init__(self, text):
        self.text = text
        self.DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.SYMBOLS = ['+', '-', '*', '/', '(', ')']
        self.tokens = []

    def run(self):
        self.tokenize()

    def tokenize(self):
        for i in range(len(self.text)):
            if self.text[i] in self.DIGITS:
                self.tokens.append(Token("Number", self.text[i], i))
            if self.text[i] in self.SYMBOLS:
                # PLUS MINUS STAR SLASH LPAREN RPAREN
                if self.text[i] == "+":
                    self.tokens.append(Token("PLUS", self.text[i], i))
                if self.text[i] == "-":
                    self.tokens.append(Token("MINUS", self.text[i], i))
                if self.text[i] == "*":
                    self.tokens.append(Token("STAR", self.text[i], i))
                if self.text[i] == "/":
                    self.tokens.append(Token("SLASH", self.text[i], i))
                if self.text[i] == "(":
                    self.tokens.append(Token("LPAREN", self.text[i], i))
                if self.text[i] == ")":
                    self.tokens.append(Token("RPAREN", self.text[i], i))
            if self.text[i] == "\n":
                self.tokens.append(Token("END", self.text[i], i))

        self.clean_up()

    def clean_up(self):
        tokens = []
        num_buf = ""
        for token in self.tokens:
            if token.type == "Number":
                num_buf += token.value
            else:
                if num_buf:
                    tokens.append(Token("Number", num_buf, token.pos))
                    num_buf = ""
                tokens.append(token)
        self.tokens = tokens

    def list_tokens(self):
        for i in self.tokens:
            print(f"Token[{i.pos}]: {i.type}({i.value})")


if __name__ == "__main__":
    with open("./ktn.ktn") as f:
        t = Tokenizer(f.read())
        t.run()
        t.list_tokens()
