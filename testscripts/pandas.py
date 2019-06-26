import pandas 
import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', "NASDAQ.csv")

df_NASDAQ=pandas.read_csv(p)

df_NASDAQ.set_index("Symbol", inplace=True)

#t1 = df_NASDAQ.iloc[1:10,4:6]
#t1 = df_NASDAQ[['Name','IPOyear','Sector','industry']]


t1 = df_NASDAQ.loc['FLWS':'QFIN',['Name','IPOyear','Sector','Industry']]

t2 = df_NASDAQ[df_NASDAQ.Sector=="Finance"][['Name','IPOyear','Sector','industry']]

#t3 = t2[t2['industry'].str.contains("Sav")]

t2['IPOyearSTR'] = t2['IPOyear'].astype(str)

#t3 = t2[t2.IPOyear > 2018]

#t3 = t2[t2['IPOyearSTR'].str.contains("18")][['Name','IPOyear','Sector','industry']]


#t3 = t2[t2.index.str.contains("Q")][['Name','IPOyear','Sector','industry']]

t3 = t2[t2.index.str.match("Z")][['Name','IPOyear','Sector','industry']]

#print(t2.dtypes)


print(t3)
