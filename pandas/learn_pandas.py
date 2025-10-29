import pandas as pd


df_class = pd.read_csv("pandas\datasets\classmarks.csv")
# print(df_class.head())

mask = df_class['group'] == 'group B'

df_class_groupB = df_class.loc[mask] #df_class['group'] == 'group B']
# print(df_class_groupB)

df_class_groupB.to_csv('pandas\datasets\classmarksgroupB.csv', index= False)
pd1 = pd.read_csv('pandas\datasets\classmarksgroupB.csv')
print(pd1)