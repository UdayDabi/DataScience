import matplotlib.pyplot as plt
x = ["Vijay", "Jay", "Ajay"]
y = [30, 90, 70]
plt.title("Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Name")
plt.grid(True)
plt.barh(x, y, color="red")
plt.show()
