import pandas as pd

sales_data = pd.read_excel("Cleaned_Dataset.xlsx")

print("Project 2 - Exploratory Data Analysis")
print("-" * 50)

print("\nDataset Overview")
print("-" * 50)

print("Rows and Columns:")
print(sales_data.shape)

print("\nColumn Names:")
print(list(sales_data.columns))

print("\nBasic Statistics")
print("-" * 50)

numeric_columns = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]

for column in numeric_columns:

    print(f"\nStatistics for {column}")
    print(sales_data[column].describe())

print("\nMost Sold Products")
print("-" * 50)

product_sales = (
    sales_data.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales)

print("\nPayment Method Usage")
print("-" * 50)

print(sales_data["PaymentMethod"].value_counts())

print("\nOrder Status Distribution")
print("-" * 50)

print(sales_data["OrderStatus"].value_counts())

print("\nReferral Source Distribution")
print("-" * 50)

print(sales_data["ReferralSource"].value_counts())

print("\nOutlier Detection (TotalPrice)")
print("-" * 50)

Q1 = sales_data["TotalPrice"].quantile(0.25)
Q3 = sales_data["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = sales_data[
    (sales_data["TotalPrice"] < lower_limit)
    | (sales_data["TotalPrice"] > upper_limit)
]

print("Number of Outliers Found:", len(outliers))
print("\nOutlier Records:")
print(outliers[["OrderID", "Product", "TotalPrice"]].to_string(index=False))
print("\nEDA completed successfully.")