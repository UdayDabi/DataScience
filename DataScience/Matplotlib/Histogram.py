import matplotlib.pyplot as plt

Marks=[321,2,1,45,1,6,2,30,4,8,59,0,20,52,206,4,26,2,66,2,220,]
bins=[0,50,100,150,200,250,300,350,400]
plt.hist(Marks, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of students')
plt.title('Histogram')
plt.show()