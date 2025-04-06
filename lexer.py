class Lexer:
    def __init__(self, text):
        print(f"Initializing lexer with text: '{text}'")
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        print(f"First character: '{self.current_char}'")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
        print(f"Advanced to character: '{self.current_char}'")

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        print(f"Parsed integer: {result}")
        return int(result)

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        print(f"Parsed identifier: {result}")
        return result

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                token = ('INTEGER', self.integer())
                print(f"Generated token: {token}")
                return token

            if self.current_char.isalpha() or self.current_char == '_':
                token = ('VARIABLE', self.identifier())
                print(f"Generated token: {token}")
                return token

            if self.current_char == '+':
                self.advance()
                token = ('PLUS', '+')
                print(f"Generated token: {token}")
                return token

            if self.current_char == '-':
                self.advance()
                token = ('MINUS', '-')
                print(f"Generated token: {token}")
                return token

            if self.current_char == '*':
                self.advance()
                token = ('MULTIPLY', '*')
                print(f"Generated token: {token}")
                return token

            if self.current_char == '/':
                self.advance()
                token = ('DIVIDE', '/')
                print(f"Generated token: {token}")
                return token

            if self.current_char == '(':
                self.advance()
                token = ('LPAREN', '(')
                print(f"Generated token: {token}")
                return token

            if self.current_char == ')':
                self.advance()
                token = ('RPAREN', ')')
                print(f"Generated token: {token}")
                return token

            if self.current_char == '=':
                self.advance()
                token = ('EQUALS', '=')
                print(f"Generated token: {token}")
                return token

            raise Exception(f'Invalid character: {self.current_char}')

        token = ('EOF', None)
        print(f"Generated token: {token}")
        return token 
