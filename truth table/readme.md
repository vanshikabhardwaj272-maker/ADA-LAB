# Truth Table Generation with Graph

## 📌 Overview
This project demonstrates **Truth Table generation** using:
- **C++** for logical operation evaluation
- **Python (Matplotlib)** for plotting truth table growth

Truth tables are used in **Digital Electronics** and **Boolean Algebra** to represent all possible input-output combinations of logic expressions.

---

 What is a Truth Table?
A truth table lists all possible combinations of input variables and their corresponding output values for a logical expression.

For `n` variables:
- Total rows = **2ⁿ**

---

 Logic Operations Used
- AND ( & )
- OR ( | )
- XOR ( ^ )
- NOT ( ! )

---

 Time Complexity
- **O(2ⁿ)**  
(because all possible combinations must be generated)

---

 Technologies Used
- C++
- Python
- Matplotlib

---

 Files Included
- `truth_table.cpp` → C++ program to generate truth table
- `graph.py` → Python code for truth table growth graph
- `README.md` → Documentation

---

 Graph Description
- **X-axis:** Number of variables
- **Y-axis:** Number of truth table rows
- Graph shows **exponential increase**, confirming O(2ⁿ)

---

 How to Run

### Run C++ Code
```bash
g++ truth_table.cpp
./a.out
