# Bitwise Operators

### What are bitwise operators?
Bitwise operators are are used for tasks where bit manipulator are required such as setting or clearing of spcific bits, combinining bits, or shifting bits left or right.

### The Operators

#### Bitwise AND (&)

Purpose: 
Performs a logical AND operation on each pair of corresponding bits of two numbers. The result has a bit set to 1 if and only if both buts in the corresponding poisiton are 1 and otherwise the resulting bit is 0

Use Case: 
Often used for masking operations to clear certain bits or check specific bits.

Example:

// 0101 in binary
int a = 5;

// 0011 in binary
int b = 3;

// 0001 in binary, 1 in decimal
int c = a & b

Visulization:

a|   0101
b| & 0011
 |-------
c| = 0001

#### Bitwise OR (|):
Purpose:
Performs a logical OR operation on each pair of corresponding bits. The result has a bit set to 1 if at least one of the bits in the corresponding position of the operands is 1.

Use Case:
Commonly used to set spcific bits in a number

Example:

// 0101 in binary
int a = 5;  

// 0011 in binary
int b = 3;  

// 0111 in binary, 7 in decimal
int c = a | b;

Visulization:

a|   0101
b| | 0011
 |-------
c| = 0111


#### Bitwise XOR (^)
Purpose:
Performs a logical exclusive OR operation on each pair of corresponding bits. The result has a bit set to 1 if exactly one of the bits in teh corresponding position of the operands is 1.

Use Case:
Useful for toggling spcific bits or finding differences between two binary values.

Example:

// 0101 in binary
int a = 5;  

// 0011 in binary
int b = 3;

// 0110 in binary, 6 in decimal
int c = a ^ b;

a|   0101
b| ^ 0011
 |-------
c| = 0110


#### Bitwise NOT (~)
Purpose: 
Inverts all the bits of a number, changing 1s to 0s and 0s to 1s.

Use Case: 
Often used to flip all bits or in conjunction with other bitwise operators for complex bit manipulations.

// 0101 in binary
int a = 5;

// 1010 in binary, -6 in decimal (assuming 4-bit representation)
int b = ~a;

#### Bitwise Shift Left (<<)
Purpose: 
Shifts the bits of the first operand left by the number of positions specified by the second operand. The vacated bits on the right are filled with 0s.

Use Case: 
Commonly used to multiply a number by 2 for each shift position.

// 0101 in binary
int a = 5;
// 1010 in binary, which is 10 in decimal
int b = a << 1;

#### Bitwise Shift Right (>>)
Purpose: 
Shifts the bits of the first operand right by the number of positions specified by the second operand. For unsigned numbers, the vacated bits on the left are filled with 0s. For signed numbers, the sign bit is copied.

Use Case: 
Commonly used to divide a number by 2 for each shift position.

Example:

// 0101 in binary
int a = 5;
// 0010 in binary, which is 2 in decimal
int b = a >> 1;