# Data Structures introduced in Python - 
# 1. Series - it is a unidirectional labelled collection of data 
# 2. Dataframe - it is a 2D-labelled collection of data


import pandas as pd

# empSeriesData = {
#     "empName": ["Rahul Tiwari", "Aman Sharma", "Shubhangi Sen", "Urvashi Rai"]
# }

# empSer = pd.Series(empSeriesData)

# print(empSeriesData)
# print(empSer)



# empDataframe = {
#     "empName": ["Rahul Tiwari", "Aman Sharma", "Shubhangi Sen", "Urvashi Rai"],
#     "empAge": [20,23,26,18],
#     "empSalary": [25000,29000,35000,50000],
#     "empResidence": ["Gurgaon", "Singapore", "Indore", "Bhopal"]
# }

# empDf = pd.DataFrame(empSeriesData)
# empDf = pd.DataFrame(empDataframe)

# print(empSeriesData)
# print(empDf)



# How to Read any DataSet in Pandas

# prod_data = pd.read_csv("prod_data_csv.csv", encoding="utf-8") #latin1 can also be used in this method
# prod_data = pd.read_json("prod_data_json.json", encoding="utf-8") #latin1 can also be used in this method
# prod_data = pd.read_excel("prod_data_excel.xlsx") 
# print(prod_data)



# empDf.to_json("demoData.json")
# empDf.to_csv("demoData.csv")
# empDf.to_excel("demoData.xlsx")
# prod_data.to_csv("demoProdData.csv")



# if we want to understant the format of the dataset quickly than we can use two methods -
# 1. .head()
# 2. .tail()


# headData = prod_data.head(10)
# tailData = prod_data.tail(10)

# print(headData)
# print(tailData)



