import matplotlib.pyplot as plt

# Number of variables
n = [1, 2, 3, 4, 5, 6]

# Number of rows in truth table = 2^n
rows = [2**i for i in n]

plt.figure()
plt.plot(n, rows)
plt.xlabel("Number of Variables (n)")
plt.ylabel("Number of Rows (2^n)")
plt.title("Truth Table Growth Graph (O(2^n))")
plt.show()
