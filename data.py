import pandas as pd

def getAllData():
    df=pd.read_csv('contacts.csv')
    return df

def updateData(data):
    df1=getAllData()
    df2 = pd.DataFrame(data)
    _newdf = df1.append(df2)
    _newdf.to_csv('contacts.csv',index=False)



