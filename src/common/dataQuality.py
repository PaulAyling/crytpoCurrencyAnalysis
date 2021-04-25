# LISTS
def cntPagedData(pagedData):
    print('Nbr Pages:          ', len(pagedData))
    print('Nbr items per page: ', len(pagedData[0]))





# DATA QUALITY (DATAFRAME)
def cnt(dataframe):
    result  = len(df.index)
    print('Nbr Rows:                ',result)
    return result
def cntDistinct(dataframe,col):
    result = len(dataframe[col].unique())
    print('Nbr Rows(Distinct Coins):',result)
    return result

def dataQualityReport(dataframe):
    cnt(dataframe)
    cntDistinct(dataframe,'name')
    # desc = dataframe["current_price"].describe()
    # print(desc)