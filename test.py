from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator
import sys

def test_simple_expression():
    with open('output.txt', 'w') as f:
        f.write("Testing simple expression: 2 + 3 * 4\n")
        f.write("-" * 40 + "\n")
        
        equation = "2 + 3 * 4"
        
        # Create lexer
        lexer = Lexer(equation)
        
        # Create parser
        parser = Parser(lexer)
        
        # Parse expression
        ast = parser.parse()
        
        # Generate code
        generator = CodeGenerator()
        generator.generate(ast)
        
        # Print instructions
        f.write("\nGenerated Instructions:\n")
        f.write("-" * 40 + "\n")
        for instruction in generator.get_instructions():
            f.write(instruction + "\n")
        
        f.write(f"\nExpected Result: {2 + 3 * 4}\n")

if __name__ == "__main__":
    test_simple_expression()
    # Read and display the output
    with open('output.txt', 'r') as f:
        print(f.read()) 
