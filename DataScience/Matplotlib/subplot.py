import matplotlib.pyplot as plt
x=["Vijay","jay","Ajay"]
y=[90,80,70]
plt.subplot(1,3,1)
plt.bar(x,y)
plt.subplot(1,3,2)
plt.scatter(x,y)
plt.subplot(1,3,3)
plt.plot(x,y,"^k")
plt.show()