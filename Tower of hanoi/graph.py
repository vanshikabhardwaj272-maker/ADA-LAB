import matplotlib.pyplot as plt

# Number of disks
n = [1, 2, 3, 4, 5, 6, 7]

# Number of moves = 2^n - 1
moves = [2**i - 1 for i in n]

plt.figure()
plt.plot(n, moves)
plt.xlabel("Number of Disks (n)")
plt.ylabel("Number of Moves")
plt.title("Tower of Hanoi Time Complexity (O(2^n))")
plt.show()
