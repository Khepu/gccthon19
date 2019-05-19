import pandas as pd
from pandas import DataFrame as df
import  numpy as np
data=pd.read_csv("datasets/website-access.data",sep=" ",header=None)

ip = data[0]





#print(tuple(filter(lambda x: int(x)>=500 and int(x)<600, data[[0]])))