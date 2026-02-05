# x Power n (Iterative and Recursive) with Graph

 Overview
This project demonstrates how to calculate **xⁿ (power of a number)** using:
- **Iterative method**
- **Recursive method**
- **Python (Matplotlib)** for plotting time complexity graph

---

 Problem Statement
Given a base `x` and power `n`, compute the value of:
xⁿ = x × x × x ... (n times)

---

 Methods Used

 Iterative Method
- Uses a loop
- Multiplies `x` repeatedly `n` times

 Recursive Method
- Uses function calls
- Breaks the problem into smaller subproblems

---

Time Complexity
- **Iterative:** O(n)
- **Recursive:** O(n)

Both methods take linear time as multiplication is done `n` times.

---

 Technologies Used
- C++
- Python
- Matplotlib

---

 Files Included
- `power_iterative.cpp` → Iterative method
- `power_recursive.cpp` → Recursive method
- `graph.py` → Time complexity graph
- `README.md` → Documentation

---

 Graph Description
- **X-axis:** Power (n)
- **Y-axis:** Time taken
- Linear growth confirms **O(n)** complexity

---

 How to Run

### Run Iterative Code
```bash
g++ power_iterative.cpp
./a.out
