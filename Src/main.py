from functions import scrapePrice,pingUrl,display,giveFxrate
import pandas as pd
import sys
from acquisition import loadDataset
from clean import cleanDataset,fixCurrencies

def main():
    #We set displaying options for Pandas dataframes
    #def set_pandas_options() -> None:
    #    pd.options.display.max_columns = 1000
    #    pd.options.display.max_rows = 1000
    #    pd.options.display.max_colwidth = 100
    #    pd.options.display.width = None
    # pd.options.display.precision = 2  # set as needed
   # set_pandas_options()

    #We load the dataset
    df=loadDataset()
    #display(df)
    dfClean=cleanDataset(df)

    #let's ping all the urls mentioned in the dataset and add the responses to the existing dataset
    #as it's a very slow process we will only do it once, save to a file and usually load the dataframe from that file
    '''
    urlStatusL=[]
    for urlElement in dfClean["url"]:
        urlStatusL.append(pingUrl(urlElement))
    print(urlStatusL) 
    dfCleanWithUrls=dfClean.insert(9,"url_status",urlStatusL,True)
    dfCleanWithUrls.to_csv('dfcleanwithurls.csv')
    '''
    dfCleanWithUrls=pd.read_csv('dfcleanwithurls.csv',encoding = "utf-8",index_col=0 )

    #We keep only those restaurants whose web is valid (the other have closed down and are not still in business)
    dfOnlyExistingRestaurants=dfCleanWithUrls[dfCleanWithUrls["url_status"] == 200]
    dfWithPriceAndC=dfOnlyExistingRestaurants.copy()

    #We will scrape the Url's for thre minimum price, maximum price and currency of each restaurant
    #Again it's a very slow process, so will onlyt do it once and load from the file. 
    '''
    minPriceL=[]
    maxPriceL=[]
    currencyL=[]
    for urlElement in dfWithPriceAndC["url"]:
        minPrice, maxPrice, currency = scrapePrice(urlElement)
        minPriceL.append(minPrice)
        maxPriceL.append(maxPrice)
        currencyL.append(currency)
    print(minPriceL)
    print(maxPriceL)
    print(currencyL)
    dfWithPriceAndC["min_price"]=minPriceL
    dfWithPriceAndC["max_price"]=maxPriceL
    dfWithPriceAndC["currency"]=currencyL
    dfWithPriceAndC.to_csv('dfWithPriceAndC.csv')
    '''
    #we're re-doing the index numbers, as we have removed some rows that had non-existing urls (i.e restaurants out of business).
    dfWithPriceAndC=pd.read_csv('dfWithPriceAndC.csv',encoding = "utf-8",index_col=0 )
    dfWithPriceAndC=dfWithPriceAndC.drop(dfWithPriceAndC.columns[[0]], axis=1)
    dfWithPriceAndC.reset_index(inplace=True,drop=True)
    #dfWithPriceAndC.to_csv('output.csv',encoding = "utf-8")

    #we fix those currencies that have null values
    dfWithPriceAndCFiltered=fixCurrencies(dfWithPriceAndC)

    #We convert the min and max prices in the dataframe to floats, in order to calculate their corresponding columns in Euros
    fx_pricelist=list(map(giveFxrate,list(dfWithPriceAndCFiltered["currency"])))
    dfWithPriceAndCFiltered["fxrate"]=[round(x,2) for x in fx_pricelist]
    min_pricelist=[float(element.replace(",","")) for element in list(dfWithPriceAndCFiltered["min_price"])]
    max_pricelist=[]
    for element in list(dfWithPriceAndCFiltered["max_price"]):
        if element is not None and isinstance(element, float)==False:
            max_pricelist.append(float(element.replace(",","")))
        else:
            max_pricelist.append(element)

    min_eurpricelist=[round(a*b,2) for a,b in zip(min_pricelist,fx_pricelist)]
    max_eurpricelist=[round(a*b,2) for a,b in zip(max_pricelist,fx_pricelist)]

    #We incorporate a min and max price column in Euros
    dfWithPriceAndCFiltered["min_eurprice"]=min_eurpricelist
    dfWithPriceAndCFiltered["max_eurprice"]=max_eurpricelist

    #display(dfWithPriceAndCFiltered)

    selectedCountry=str(sys.argv[1])
    print("selectedCountry is:")
    print(selectedCountry)
    selectedStars=int(sys.argv[2])
    print("selectedStars is:")
    print(selectedStars)
    resultingDf=dfWithPriceAndCFiltered[(dfWithPriceAndCFiltered["country"]==selectedCountry) & (dfWithPriceAndCFiltered["stars"]==selectedStars)]
    resultingDf=resultingDf.sort_values(by="min_eurprice")
    resultingDf.reset_index(inplace=True,drop=True)
    display(resultingDf.truncate(after=2))
                
if __name__ == '__main__':
    main()


