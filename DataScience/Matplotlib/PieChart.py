import matplotlib.pyplot as plt
x = ["Vijay", "Jay", "Ajay"]
y=[12,27,60]

ex=[0.1,0,0]
colors=["red","blue","green"]
plt.pie(y,ex,labels=x,colors=colors,autopct="%1.1f%%",shadow=True,startangle=90)
plt.title("Pie Chart")
plt.legend(loc="lower left")
plt.show()