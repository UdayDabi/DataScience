import pandas as pd

s =pd.Series([1, 2, 3, 4, 5])
print(s)
print(type(s))
print('shape',s.shape)
print('',s.size)
print(s.index)
print(s.ndim)
print(s.dtype)
print(s.nbytes)
print(s.empty)
print(s.hasnans)

