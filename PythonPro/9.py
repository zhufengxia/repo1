"""
from time import sleep 
from tqdm import tqdm 

for i in tqdm(range(100)):
    sleep(0.1)
"""
""""
from os.path import join
s='abc'
k=','.join(s)
print(type(k))
"""
""""
import pandas as pd
ret=[1,2,3,4,5]
df = pd.DataFrame(ret, columns=['colname']) .rename(columns={"colname":"666"})
print(df)
"""

i=[1]


[i for _ in range(10)]

print(i)
