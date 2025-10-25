import  numpy as np

arr =np.array([[1,2,3],[4,5,6]])
np.save('data.npy',arr)
load_arr= np.load('data.npy')
print(load_arr)