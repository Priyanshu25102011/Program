import pandas as pd
import numpy as np
Sports_Tournament = {'name':['John','Smith','Alice','Bob','Diana','Eve','Charlie','Austin'],
                'team':['A','B','A','B','A','B','A','B'],
                'Goals':[15 , 20 , 25 , np.nan , 30 , 18 , 22 , np.nan],
                'Assists':[5 , 7 , 10 , 6 , 8 , 9 , 11 , 4]}
Judges = ['J1' , 'J2' , 'J3' , 'J4' , 'J5' , 'J6' , 'J7' , 'J8']
df = pd.DataFrame(Sports_Tournament , index=Judges)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())