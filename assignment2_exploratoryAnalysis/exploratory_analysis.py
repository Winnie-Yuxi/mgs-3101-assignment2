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

# Display descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())
# Display the median for numerical columns
print("\nMedian Values:")
print(df.median(numeric_only=True))

# Group data by product category
print("\nTotal Quantity Sold by Product Category:")
category_sales = df.groupby("product_category")["transaction_qty"].sum()
print(category_sales.sort_values(ascending=False))

# Find the highest and lowest unit prices
print("\nHighest Unit Price:")
highest_price = df["unit_price"].max()
print(highest_price)
print("\nRow(s) with Highest Unit Price:")
print(df[df["unit_price"] == highest_price])
print("\nLowest Unit Price:")
lowest_price = df["unit_price"].min()
print(lowest_price)
print("\nRow(s) with Lowest Unit Price:")
print(df[df["unit_price"] == lowest_price])

highest_price = df["unit_price"].max()
lowest_price = df["unit_price"].min()