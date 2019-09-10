from functions import display
def cleanDataset(inputDf):
    import pandas as pd
    #We drop the columns of price, zipcode and year
    df=inputDf.drop(columns=["price","zipCode","year"])

    #let's see which rows have null values.
    #print(df.isnull().sum())
    #print(df[df["city"].isnull()])

    # We will fix the rows that have Nan values
    df.at[152,'city']="Hong Kong"
    df.at[166,'city']="Hong Kong"

    #Let's check if there's no more null values
    #print(df.isnull().sum())
    #print(df.head(10))

    # We are going to create a column for the country, copying it from the region, as replacing those regions which are not countries for the corresponding country
    df.insert(6, "country", df["region"], True)
    df["country"]=df["country"].replace("California", "United States")
    df["country"]=df["country"].replace("Chicago", "United States")
    df["country"]=df["country"].replace("New York City", "United States")
    df["country"]=df["country"].replace("Washington DC", "United States")
    df["country"]=df["country"].replace("Hong Kong", "China")
    df["country"]=df["country"].replace("Macau", "China")
    df["country"]=df["country"].replace("Rio de Janeiro", "Brasil")
    df["country"]=df["country"].replace("Sao Paulo", "Brasil")
    df["country"]=df["country"].replace("Taipei", "Taiwan")
    return df


def fixCurrencies(inputDf):
    df=inputDf.copy()
    df.at[164,'currency']="HKD"
    df.at[176,'currency']="HKD"
    df.at[575,'currency']="HKD"
    df.at[577,'currency']="HKD"
    df.at[581,'currency']="HKD"
    df.at[669,'currency']="HKD"

    df.at[373,'currency']="THB"
    df.at[382,'currency']="THB"
    df.at[390,'currency']="THB"
    df.at[628,'currency']="THB"
    df.at[630,'currency']="THB"

    df.at[362,'currency']="TWD"
    df.at[364,'currency']="TWD"
    df.at[367,'currency']="TWD"
    df.at[626,'currency']="TWD"
    #rint(df.at[614,'currency'])
    #print(df.at["614",'name'])
    df.at[613,'currency']="SGD"
    #print(df.iloc[[614],[2,13]])
    #print(df.at[614,'currency'])
    return df
    