class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token[0] == 'INTEGER':
            self.eat('INTEGER')
            return {'type': 'INTEGER', 'value': token[1]}
        elif token[0] == 'VARIABLE':
            self.eat('VARIABLE')
            return {'type': 'VARIABLE', 'name': token[1]}
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            self.error()

    def term(self):
        node = self.factor()
        while self.current_token[0] in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token[0] == 'MULTIPLY':
                self.eat('MULTIPLY')
            elif token[0] == 'DIVIDE':
                self.eat('DIVIDE')
            node = {
                'type': 'BINARY_OP',
                'left': node,
                'op': token[1],
                'right': self.factor()
            }
        return node

    def expr(self):
        node = self.term()
        while self.current_token[0] in ('PLUS', 'MINUS'):
            token = self.current_token
            if token[0] == 'PLUS':
                self.eat('PLUS')
            elif token[0] == 'MINUS':
                self.eat('MINUS')
            node = {
                'type': 'BINARY_OP',
                'left': node,
                'op': token[1],
                'right': self.term()
            }
        return node

    def assignment(self):
        if self.current_token[0] == 'VARIABLE':
            var_name = self.current_token[1]
            self.eat('VARIABLE')
            if self.current_token[0] == 'EQUALS':
                self.eat('EQUALS')
                expr_node = self.expr()
                return {
                    'type': 'ASSIGNMENT',
                    'name': var_name,
                    'value': expr_node
                }
        return self.expr()

    def parse(self):
        return self.assignment() 
