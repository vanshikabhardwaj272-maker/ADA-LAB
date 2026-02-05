import matplotlib.pyplot as plt

# Input size
n = [10, 50, 100, 200, 500, 1000]

# Time taken (quadratic growth - O(n^2))
time = [1, 25, 100, 400, 2500, 10000]

plt.figure()
plt.plot(n, time)
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken")
plt.title("Bubble Sort Time Complexity Graph (O(n²))")
plt.show()
