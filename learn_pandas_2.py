import pandas as pd



if __name__ == '__main__':
    data_q1 = pd.read_csv("/root/dataset_workbook/pythondatalearning/sales_report_1.csv")
    data_q2 = pd.read_csv("/root/dataset_workbook/pythondatalearning/sales_report_2.csv")
    data_unit1 = pd.read_csv("/root/dataset_workbook/pythondatalearning/sales_report_unit_1.csv")
    data_unit2 = pd.read_csv("/root/dataset_workbook/pythondatalearning/sales_report_unit_2.csv")

    stack_output_1 = pd.concat([data_q1,data_unit1],axis=1)
    stack_output_2 = pd.concat([data_q2,data_unit2],axis=1)

    stack_output = pd.concat([stack_output_1,stack_output_2], axis=0)
    stack_output = stack_output[["Year", "Month", "Sales", "unit"]]
    print(stack_output)
    stack_output.to_csv("full_month.csv", index= False)



    # datasave = pd.concat([data_q1,data_unit1], axis=1)
    # print(datasave[['Year','Month','Sales', 'unit']])
