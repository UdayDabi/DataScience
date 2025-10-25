import numpy as np
list1=[10,20,30,40,50,60,70]
array1=np.array(list1,dtype=float)
print(array1)
type(array1)

list2 = [[10, 20, 30, 40], [50, 60, 70, 60]]
array2 = np.zeros((2, 4))
print(array2)

list3 = [[10, 20, 30, 40], [50, 60, 70, 60]]
array3 = np.ones((1,5))
print(array3)

list4 = [[10, 20, 30, 40], [50, 60, 70, 60]]
array4 = np.arange(1,5,2)
print(array4)

list5 = [[10, 20, 30, 40], [50, 60, 70, 60]]
array5 = np.linspace(1,5,2)
print(array5)