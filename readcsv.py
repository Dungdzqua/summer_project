#doc csv
import pandas as pd

mycsv=pd.read_csv('data2.csv')
df=pd.DataFrame(mycsv)
shuffled_df = df.sample(n=len(df))
shuffled_df = shuffled_df.reset_index(drop=True)
csvList=shuffled_df.values