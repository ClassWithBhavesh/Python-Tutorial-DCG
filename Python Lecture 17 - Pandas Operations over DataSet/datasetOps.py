# Dataset Operation 

import pandas as pd

dataFrame = pd.read_csv("MOCK_DATA.csv")
# print(dataFrame)

# tp target a column dataset
# pro_names = dataFrame['Prod_Name']
# print(pro_names)


# to target multiple column dataset
# columnData = dataFrame[['Prod_Name', 'Prod_des', 'Prod_Cat']]
# print(columnData)


# filtering data on behalf of single condition
# filteredData = dataFrame[dataFrame['Prod_Price'] > 2]
# print(filteredData)


# for multiple condition - 
filteredData = dataFrame[(dataFrame['Prod_Price'] > 2) & (dataFrame['Prod_Cat'] == "Health")]
print(filteredData)


