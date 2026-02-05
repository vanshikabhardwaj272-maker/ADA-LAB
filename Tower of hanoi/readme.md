# Tower of Hanoi Algorithm with Graph

 Overview
This project demonstrates the **Tower of Hanoi problem** using:
- **C++** for recursive implementation
- **Python (Matplotlib)** for plotting the time complexity graph

Tower of Hanoi is a classic recursive problem involving moving disks between rods following specific rules.

---

 Problem Statement
Given three rods (Source, Auxiliary, Destination) and `n` disks:
- Only one disk can be moved at a time
- A larger disk cannot be placed on a smaller disk
- Move all disks from Source to Destination

---

 Algorithm (Recursive)
1. Move `n-1` disks from Source to Auxiliary
2. Move the nth disk from Source to Destination
3. Move `n-1` disks from Auxiliary to Destination

---

 Time Complexity
- **Time Complexity:** O(2ⁿ)
- **Total Moves Required:** 2ⁿ − 1

---

 Technologies Used
- C++
- Python
- Matplotlib

---

 Files Included
- `tower_of_hanoi.cpp` → C++ recursive program
- `graph.py` → Python code for time complexity graph
- `README.md` → Project documentation

---

 Graph Description
- **X-axis:** Number of disks (n)
- **Y-axis:** Number of moves
- Exponential curve confirms **O(2ⁿ)** complexity

---

How to Run

### Run C++ Code
```bash
g++ tower_of_hanoi.cpp
./a.out
