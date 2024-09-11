# Leetcode 206: Reverse a Linked List

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]

Example 2:

Input: head = []

Output: []


Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

#### Idea
The trick behind this problem is always keeping track of where you just were and where your at now. To do this use two pointers in C++, or two objects in Python. It is also important to note what the end condition should be? In other words how do you know when all the nodes have been switched?
To accomplish this you need to have two variables that keep track of your past node and your current node, then when the current node is a nullptr or None you know you have reached the end of the list.
Finally to update the root you set root node equal to the prev node.

#### Starting Case:
The starting case for C++ is that you havent been anywhere yet so:

(C++):
PrevPtr = nullptr
CurrPtr = root

(Python):
PrevNode = None
CurrNode = root


#### Switch Case
The switch case is that the node you are currently looking at is not empty

(C++):

// declare a new node temp, this will be used to update curr later
TreeNode* tempPtr = CurrPtr->next;

// have the current node point to the previous to switch it's position
CurrPtr->next = PrevPtr;

// update prev node to curr node so we can find it on the next round of swtiching
PrevPtr = CurrPtr;

// update curr node to the temp node
CurrPtr = tempPtr;

(Pyton):

\# set a temp ListNode to update currNode with later
tempNode = currNode.next

\# have currNode point to the prev node
currNode.next = prevNode

\# update the prev object to the curr object
prevNode = currNode

\# set curr equal to the emp object
currNode = tempNode


#### Pseudo Code:

1. check if the root node is valid and points to something:
    if does not return root
    if it does continue

2. Set the inital values for the prevNode to null/None and the currNode to the root of the linked list

3. while the current node is not null/None
    a. create a temp node to hold the next address/object
    b. have the current node point to the previous node
    c. set the previous node to the current node
    d. set the current node to the temp node

4. set the head node = prev node 

5. return the head node

To-Do Update the Code for this list