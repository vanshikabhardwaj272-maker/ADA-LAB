import matplotlib.pyplot as plt

# Value of n (power)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Time complexity O(n) (simulated)
time = [i for i in n]

plt.figure()
plt.plot(n, time)
plt.xlabel("Power (n)")
plt.ylabel("Time Taken")
plt.title("Time Complexity of x^n (Iterative & Recursive) - O(n)")
plt.show()
