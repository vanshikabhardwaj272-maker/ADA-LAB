import matplotlib.pyplot as plt

# Number of elements
n = [10, 50, 100, 200, 500, 1000]

# Time taken (linear growth)
time = [1, 5, 10, 20, 50, 100]

plt.figure()
plt.plot(n, time)
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken")
plt.title("Linear Search Time Complexity (O(n))")
plt.show()
