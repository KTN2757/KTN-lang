import lexer


class Parser:
    def __init__(self, text: str):
        t = lexer.Tokenizer(text)
        t.run()
        t.list_tokens()

    def run(self):
        pass


if __name__ == "__main__":
    p = Parser("1+2")
    p.run()
