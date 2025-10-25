import matplotlib.pyplot as plt
x = ["Vijay", "Jay", "Ajay"]
y = [90, 80, 70]
plt.title("Bar Graph")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.grid(True)
plt.bar(x, y, color="purple")
plt.show()