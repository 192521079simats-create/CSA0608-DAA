import matplotlib.pyplot as plt
import numpy as np
import os

sizes = ["5 Events", "50 Events", "500 Events"]

greedy = [0.000170, 0.000883, 0.067153]
dynamic = [0.000147, 0.000213, 0.000637]
merge = [0.000082, 0.000277, 0.000989]

x = np.arange(len(sizes))
width = 0.25

plt.figure(figsize=(10, 6))

plt.bar(x - width, greedy, width, label="Greedy")
plt.bar(x, dynamic, width, label="Dynamic Programming")
plt.bar(x + width, merge, width, label="Merge Sort")

plt.yscale("log")
plt.xlabel("Dataset Size")
plt.ylabel("Execution Time (Seconds)")
plt.title("EventSphere X - Performance Comparison")
plt.xticks(x, sizes)
plt.legend()
plt.grid(axis="y")

plt.tight_layout()
os.makedirs("Output_Screenshots", exist_ok=True)

plt.savefig(
    os.path.join("Output_Screenshots", "10_Performance_Graph.png")
)

plt.show()