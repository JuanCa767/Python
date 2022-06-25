import pandas as pd
import numpy as np

#metodo where
#df = pd.DataFrame(np.arange(12).reshape([4,3]))# empieza en cero
df = pd.DataFrame(np.arange(1,13).reshape([4,3]), index=['a','b','c','d'], columns=['A','B','C'])
#Con el index se nombran las filas y con columns las colimnas.
print(df)

r= df.where(df%2==0)
print(r)
#recorrer el dataframe
