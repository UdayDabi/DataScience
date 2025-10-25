import pandas as pd

a = pd.Series(['Java','C', 'C++','Python'])
print(a.map({'Java':'Core', 'C':'javaScript'}))

print(a)
