import pandas as pd



if __name__ == '__main__':
    #DATASET DF COMBINATIONS

    #CONCAT --> rowise columnwise combinig
    #MERGE  --> 2 datasets merging with common columns [equ to SQL join]
    #JOIN   --> 2 datasets joining by indexing...

    data_q1 = pd.read_csv("/root/dataset_workbook/pythondatalearning/name_details.csv")
    data_q2 = pd.read_csv("/root/dataset_workbook/pythondatalearning/designation_data.csv")

    print(data_q2)
    data_q2 = data_q2.set_index("id")
    print(data_q2)

    result = data_q1.join(data_q2, on="id")

    print(result.columns)
    print(result)


    result["email"] = result[' name'].apply(lambda name: name+"@bmwtechworks.in")

    result["codenumber"] = result['id'].apply(lambda name: int(name)+66)

    # lambda -- for loop

    print(result)

    # name = ["Ashwin","Haripriya", "Ashok", "AADH"]
    # email = name+ "@bmwtechworks.in"
    # print(email)

#NAN  *PERFOMANCE

    # datares= pd.merge(data_q1,data_q2,on="id",how="outer")
    #
    # print(datares)
    #
    # datares.to_csv("data_res.csv",index=False)

    # datasave = pd.concat([data_q1,data_unit1], axis=1)
    # print(datasave[['Year','Month','Sales', 'unit']])





# * LOAD
# * GROUP
# *FILTER
# *PIVOT
# *joining - concat, merge , join
# *apply

