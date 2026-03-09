import pandas as pd



if __name__ == '__main__':
    save = True
    data = pd.read_csv("/root/dataset_workbook/pythondatalearning/WB_population_cleaned.csv", names=["countrycode","country","year","population_count"], header= 1)
    # data.head()
    # data.shape, data.columns
    # data.to_csv("saved_popluation.csv", index=False)
    # print("end")


    # data_2024 = data[data['year']==2024]
    # print(data_2024)
    # print(data_2024.info())
    # print(data_2024.shape)
    #
    # data2024_cleaned = data_2024.dropna()
    # print(data2024_cleaned.shape)
    # print(data_2024.shape)


    # data_2024.fillna("unknown", inplace=True)
    #
    data["countrycode"] = data["countrycode"].fillna("Unknown")
    #
    # data_2024.to_csv("saved_popluation.csv", index=False)

    # yearwisepops = data.groupby("year")["count"].sum()
    # print(yearwisepops)

    # data["growth"] = (data["count"].pct_change() * 100),2

    # data["growth"] = data["count"].pct_change() * 100

    # data["growth"] = round((data["count"].pct_change() * 100),2)
    # data.to_csv("saved_pop_percent.csv", index=False)

    data["year"] = data["year"].astype(int)

    print(data)


    # print(data.loc[data["year"].idxmax()])

    # latest = data.sort_values("year").groupby("country").tail(1)
    # # print(latest)
    # latest.to_csv("latest_year.csv", index=False)

    # print(data.loc[data["countrycode"] == "AFE"])
    # data.to_csv("locs.csv", index=False)

    # print(data.loc[(data["countrycode"] == "IND") & (data["year"] >= 2020), ["year", "count"]])




#NOTES:
#header
#loc for filtering by columns & conditions
#iloc for selecting by numbers (index)
#concat , merge , join
#pivot


#EXERCISE:
# Load the CSV file into a DataFrame
# Show first 5 rows
# Select only country and population
# Get rows where population > 740000000
# Group by country and get average population
# Get latest population for each country

    pivoted_countrywisedata = pd.pivot_table(data,
                                                 values="population_count",
                                                 index="country",
                                                 columns="year",
                                                 aggfunc="sum"
                                                 )
    pivoted_countrywisedata.to_csv('pivoted_data.csv')
    # pivoted_countrywisedata.to_excel("population_pivot_2022_onwards.xlsx")
    # print("pivoted_countrywisedata", pivoted_countrywisedata)



