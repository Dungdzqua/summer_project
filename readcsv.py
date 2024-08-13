#doc csv
import pandas as pd

mycsv=pd.read_csv('data2.csv')
df=pd.DataFrame(mycsv)
csvList=df.values