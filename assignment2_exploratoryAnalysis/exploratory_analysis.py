import pandas as pd

df = pd.read_csv("data/Coffee_Shop_Sales.csv")
print("Coffee shop dataset loaded successfully.")

# Display the number of rows and columns.
print("\nDataset shape:")
print(df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Display the data type of each column.
print("\nColumn data types:")
print(df.dtypes)

# Display the first five rows.
print("\nFirst five rows:")
print(df.head())

# Count missing values in each column.
print("\nMissing values in each column:")
print(df.isna().sum())