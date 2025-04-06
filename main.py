from lexer import Lexer
from parser import Parser
from code_generator import CodeGenerator

def compile_equation(equation, output_file, generator):
    try:
        # Create the lexer
        lexer = Lexer(equation)
        
        # Create the parser
        parser = Parser(lexer)
        
        # Parse the equation into an AST
        ast = parser.parse()
        
        # Generate custom instructions
        result_reg = generator.generate(ast)
        
        # If this was an assignment, store the result
        if ast['type'] == 'ASSIGNMENT':
            var_name = ast['name']
            if var_name not in generator.variables:
                generator.variables[var_name] = generator.new_register()
            target_reg = generator.variables[var_name]
            generator.add_instruction(f'MOV {target_reg}, {result_reg}', f'Store into variable {var_name}')
        
        # Return the generated instructions
        return generator.get_instructions()
    except Exception as e:
        print(f"Error during compilation: {str(e)}")
        return []

def print_help():
    print("\nAvailable commands:")
    print("1. var = value    (e.g., 'x = 5' to assign value to variable)")
    print("2. expression     (e.g., 'x + y * 2' to evaluate expression)")
    print("3. vars           (to show all defined variables)")
    print("4. help          (to show this help message)")
    print("5. exit          (to quit the program)")
    print("\nNote: Variable names can only contain letters and numbers")
    print("Supported operators: +, -, *, /")

def show_variables(generator):
    if not generator.variables:
        print("\nNo variables defined yet")
        return
    
    print("\nDefined variables:")
    print("-" * 20)
    for var_name in generator.variables:
        value = generator.var_values.get(var_name, "undefined")
        print(f"{var_name} = {value}")

def main():
    print("\nWelcome to the Interactive Equation Compiler!")
    print("=" * 50)
    print_help()
    
    generator = CodeGenerator()
    
    while True:
        try:
            # Get user input
            equation = input("\nEnter an equation (or command): ").strip()
            
            # Handle commands
            if equation.lower() == 'exit':
                print("Goodbye!")
                break
            elif equation.lower() == 'help':
                print_help()
                continue
            elif equation.lower() == 'vars':
                show_variables(generator)
                continue
            elif not equation:
                continue
            
            # Compile the equation
            print("\nCompiling:", equation)
            print("-" * 40)
            
            instructions = compile_equation(equation, None, generator)
            
            if instructions:
                print("\nGenerated Instructions:")
                print("-" * 40)
                for instruction in instructions:
                    print(instruction)

                # Evaluate the final result if possible
                last_var = None
                if '=' in equation:
                    # Assignment, get the variable on the left-hand side
                    last_var = equation.split('=')[0].strip()
                else:
                    # Expression, store result in special variable (e.g., "_")
                    last_var = "_"

                if last_var in generator.var_values:
                    print(f"\nEvaluated Result: {generator.var_values[last_var]}")
                else:
                    print("\nNote: Could not evaluate result (value may be undefined)")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Type 'help' for usage information")

if __name__ == "__main__":
    main() 
