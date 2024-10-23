# Node
A binary tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. This structure is widely used in computer science for various applications, including searching, sorting, and representing hierarchical data.

Key Concepts
Node: The fundamental part of a binary tree. Each node contains:

Data: The value stored in the node.
Left Child: A pointer/reference to the left child node (can be null if no child exists).
Right Child: A pointer/reference to the right child node (can be null if no child exists).
Types of Binary Trees:

Full Binary Tree: Every node has either 0 or 2 children.
Complete Binary Tree: All levels are fully filled except possibly for the last level, which is filled from left to right.
Perfect Binary Tree: All internal nodes have two children, and all leaf nodes are at the same level.
Balanced Binary Tree: The height of the left and right subtrees of any node differ by at most one.
Binary Search Tree (BST): A binary tree where the left child contains values less than the parent node, and the right child contains values greater.
Traversal Methods:

In-order Traversal: Visit the left subtree, the node, and then the right subtree (results in sorted order for BSTs).
Pre-order Traversal: Visit the node first, then the left subtree, followed by the right subtree.
Post-order Traversal: Visit the left subtree, the right subtree, and then the node.
Applications:

Searching and Sorting: BSTs allow for efficient searching, insertion, and deletion operations.
Expression Trees: Used in compilers to represent mathematical expressions.
Heap Structures: Binary trees are used in implementing heaps for priority queues.
Height and Depth:

Height of a Tree: The length of the longest path from the root to a leaf. A tree with only one node has a height of 0.
Depth of a Node: The number of edges from the root to that node
