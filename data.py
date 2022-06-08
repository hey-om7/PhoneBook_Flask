import pandas as pd

def getAllData():
    df=pd.read_csv('contacts.csv')
    return df


contacts=[
    {'name':'John Doe', 'phone':'555-555-5555'},
    {'name':'Jane Doe', 'phone':'222-555-5555'},
    {'name':'Joe Doe', 'phone':'333-555-5555'},
    {'name':'Jill Doe', 'phone':'444-555-5555'},
    {'name':'Jack Doe', 'phone':'555-555-5555'},
    {'name':'Jill Doe', 'phone':'444-555-5555'},
    {'name':'Jack Doe', 'phone':'555-555-5555'},
]


def updateData(data):
    df1=getAllData()
    df2 = pd.DataFrame(data,index=[len(df1)])
    _newdf = df1.append(df2)
    _newdf.to_csv('contacts.csv')