
# Custom Instruction Simulation – MULADD
This project simulates a custom compiler instruction called `MULADD`, which optimizes the equation:
z = (a * b) + (c * d)

##Instruction Details

Instruction: MULADD
Syntax: MULADD Rz, Ra, Rb, Rc, Rd
Operation: `Rz = (Ra * Rb) + (Rc * Rd)


##C Code Simulation
We simulate this in C using a function MULADD(a, b, c, d)

 Sample Output: 
 Enter values: 2 3 4 5
 Result: 26
