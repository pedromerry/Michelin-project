def loadDataset():
    import pandas as pd
    import os
    currentPath=os.getcwd().split("\\Src") 
    print(currentPath)
    #We load the three datasets
    sourcePathDataSet1Star = str(currentPath[0]) + "\\Input\\one-star-michelin-restaurants.csv"
    sourcePathDataSet2Star = str(currentPath[0]) + "\\Input\\two-stars-michelin-restaurants.csv"
    sourcePathDataSet3Star = str(currentPath[0]) + "\\Input\\three-stars-michelin-restaurants.csv"

    df1Star = pd.read_csv(sourcePathDataSet1Star)
    df2Star = pd.read_csv(sourcePathDataSet2Star)
    df3Star = pd.read_csv(sourcePathDataSet3Star)

    #We introduce a new column for the number of stars in each dataframe
    df1Star.insert(0, "stars", [1 for i in range(df1Star.shape[0])], True)
    df2Star.insert(0, "stars", [2 for i in range(df2Star.shape[0])], True)
    df3Star.insert(0, "stars", [3 for i in range(df3Star.shape[0])], True)

    #We merge the three data frames by stacking them one on top of the other
    outputDf = pd.concat([df1Star, df2Star, df3Star]).reset_index(drop=True)
    return outputDf