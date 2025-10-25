import matplotlib.pyplot as plt
plt.title("Line Graph")
plt.ylabel("Y-Axis Label")
plt.xlabel("X-Axis Label")
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'o')  # 'o' specifies dot markers
plt.show()