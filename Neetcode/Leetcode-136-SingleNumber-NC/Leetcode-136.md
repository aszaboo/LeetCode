## Single Number
You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

#### Example 1:

Input: nums = [3,2,3]

Output: 2

#### Example 2:

Input: nums = [7,6,6,7,8]

Output: 8


#### Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000

### Idea:
The idea for this problem is to use bitwise operators to lead to the eventuall end value. Here the XOR (^) operator will be appied to each element in the list and then the resulting number will be added to the current value. 

XOR Selection:
In this case the XOR operator is selected as when you have an even quantity of an integer calling XOR will cancel out these bits making the number equal to zero.

Example:

Lets say I first apply the operator on integers 5 and 3.

int a = 5;  // 0101 in binary
int b = 3;  // 0011 in binary
int c = a ^ b;  // 0110 in binary, which is 6 in decimal

Now lets say I apply the bitwise operator to the result of this

int a = 5 // 0101 in binary
int c = 6 // // 0110 in binary
int d = a ^ c // 0011 // 3 in binary

This shows although the XOR operator may be applied on a sum:
(a + b) ^ b = a. 

This property is what will allow us to determine what the Single Number in the list is

#### Pseudo Code

1. create a container to hold the sum of the integers so far
2. loop over each int in the array, and apply the bitwise operator between the current number and the sum, then add it to the sum (sum = sum ^ num)
3. return the sum variable