#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include<bits/stdc++.h>
using namespace std;

class CodeGenerator {
public:
    map<string, string> variables;
    map<string, int> var_values;
    vector<string> instructions;
    int reg_count = 0;

    string new_register() {
        return "R" + to_string(reg_count++);
    }

    void add_instruction(string instr, string comment = "") {
        if (!comment.empty()) {
            instr += " ; " + comment;
        }
        instructions.push_back(instr);
    }

    string generate_expression(const string& expression) {
        // For demo: just simulate one operation (e.g., x + y)
        istringstream iss(expression);
        string a, op, b;
        iss >> a >> op >> b;

        string reg1 = variables.count(a) ? variables[a] : new_register();
        string reg2 = variables.count(b) ? variables[b] : new_register();

        if (!variables.count(a)) {
            variables[a] = reg1;
            add_instruction("MOV " + reg1 + ", " + a, "load " + a);
        }
        if (!variables.count(b)) {
            variables[b] = reg2;
            add_instruction("MOV " + reg2 + ", " + b, "load " + b);
        }

        string result = new_register();
        string instr = op == "+" ? "ADD" : op == "-" ? "SUB" : op == "*" ? "MUL" : "DIV";
        add_instruction(instr + " " + result + ", " + reg1 + ", " + reg2);

        return result;
    }

    void clear_instructions() {
        instructions.clear();
    }

    vector<string> get_instructions() {
        return instructions;
    }
};

void print_help() {
    cout << "\nAvailable commands:\n";
    cout << "1. var = value (e.g., x = 5)\n";
    cout << "2. expression (e.g., x + y)\n";
    cout << "3. vars (view variables)\n";
    cout << "4. help\n";
    cout << "5. exit\n";
    cout << "Supported: +, -, *, /\n";
}

void show_variables(CodeGenerator& gen) {
    if (gen.variables.empty()) {
        cout << "No variables defined.\n";
        return;
    }
    for (auto& var : gen.variables) {
        cout << var.first << " = " << var.second << endl;
    }
}

int main() {
    CodeGenerator gen;
    string input;

    cout << "\nInteractive Equation Compiler (C++ Version)\n";
    print_help();

    while (true) {
        cout << "\nEnter input: ";
        getline(cin, input);

        if (input == "exit") break;
        if (input == "help") {
            print_help();
            continue;
        }
        if (input == "vars") {
            show_variables(gen);
            continue;
        }

        gen.clear_instructions();

        if (input.find('=') != string::npos) {
            string var = input.substr(0, input.find('='));
            string val = input.substr(input.find('=') + 1);
            var.erase(remove(var.begin(), var.end(), ' '), var.end());
            val.erase(remove(val.begin(), val.end(), ' '), val.end());

            string reg = gen.new_register();
            gen.variables[var] = reg;
            gen.var_values[var] = stoi(val);
            gen.add_instruction("MOV " + reg + ", " + val, "Assign value to " + var);
        } else {
            string result = gen.generate_expression(input);
            gen.add_instruction("PRINT " + result, "Output result");
        }

        cout << "\nGenerated Instructions:\n";
        for (string& instr : gen.get_instructions()) {
            cout << instr << endl;
        }
    }

    cout << "Goodbye!\n";
    return 0;
}
