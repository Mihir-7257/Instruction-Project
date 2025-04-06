#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <iomanip>
#include <any>  

using namespace std;

class CodeGenerator {
public:
    int register_count = 0;
    map<string, string> variables;
    map<string, int> var_values;
    vector<string> instructions;

    string new_register() {
        return "R" + to_string(register_count++);
    }

    void add_instruction(string instruction, string comment) {
        ostringstream oss;
        oss << left << setw(30) << instruction << " ; " << comment;
        instructions.push_back(oss.str());
    }

    pair<string, int> generate(map<string, any>& node) {
        string node_type = any_cast<string>(node["type"]);

        if (node_type == "INTEGER") {
            int value = any_cast<int>(node["value"]);
            string reg = new_register();
            add_instruction("LOAD " + reg + ", " + to_string(value), "Load constant " + to_string(value));
            return {reg, value};
        }

        if (node_type == "VARIABLE") {
            string var_name = any_cast<string>(node["name"]);
            if (variables.find(var_name) == variables.end()) {
                throw runtime_error("Undefined variable: " + var_name);
            }
            string reg = new_register();
            string var_reg = variables[var_name];
            add_instruction("MOV " + reg + ", " + var_reg, "Load variable " + var_name);
            return {reg, var_values[var_name]};
        }

        if (node_type == "ASSIGNMENT") {
            auto value_node = any_cast<map<string, any>>(node["value"]);
            auto [value_reg, value] = generate(value_node);
            string var_name = any_cast<string>(node["name"]);

            if (variables.find(var_name) == variables.end()) {
                variables[var_name] = new_register();
            }
            string target_reg = variables[var_name];
            add_instruction("MOV " + target_reg + ", " + value_reg, "Store into variable " + var_name);
            var_values[var_name] = value;
            return {target_reg, value};
        }

        if (node_type == "BINARY_OP") {
            auto left_node = any_cast<map<string, any>>(node["left"]);
            auto right_node = any_cast<map<string, any>>(node["right"]);

            auto [left_reg, left_val] = generate(left_node);
            auto [right_reg, right_val] = generate(right_node);

            string op = any_cast<string>(node["op"]);
            string result_reg = new_register();
            int result = 0;

            if (op == "+") {
                result = left_val + right_val;
                add_instruction("ADD " + result_reg + ", " + left_reg + ", " + right_reg, "Add " + left_reg + " and " + right_reg);
            } else if (op == "-") {
                result = left_val - right_val;
                add_instruction("SUB " + result_reg + ", " + left_reg + ", " + right_reg, "Subtract " + right_reg + " from " + left_reg);
            } else if (op == "*") {
                result = left_val * right_val;
                add_instruction("MUL " + result_reg + ", " + left_reg + ", " + right_reg, "Multiply " + left_reg + " by " + right_reg);
            } else if (op == "/") {
                result = left_val / right_val;
                add_instruction("DIV " + result_reg + ", " + left_reg + ", " + right_reg, "Divide " + left_reg + " by " + right_reg);
            }

            return {result_reg, result};
        }

        throw runtime_error("Unknown node type");
    }

    vector<string> get_instructions() {
        return instructions;
    }
};

int main() {
    CodeGenerator generator;

    // Example AST for: x = 5 + 2
    map<string, any> int_node_left = {
        {"type", string("INTEGER")},
        {"value", 5}
    };

    map<string, any> int_node_right = {
        {"type", string("INTEGER")},
        {"value", 2}
    };

    map<string, any> bin_op_node = {
        {"type", string("BINARY_OP")},
        {"op", string("+")},
        {"left", int_node_left},
        {"right", int_node_right}
    };

    map<string, any> assign_node = {
        {"type", string("ASSIGNMENT")},
        {"name", string("x")},
        {"value", bin_op_node}
    };

    // Generate code
    generator.generate(assign_node);

    // Print instructions
    cout << "Generated Instructions:\n-------------------------\n";
    for (const auto& instr : generator.get_instructions()) {
        cout << instr << endl;
    }

    return 0;
}
