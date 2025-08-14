import pandas as pd

# Read CSV with proper encoding
df = pd.read_csv("Data\Raw_Data\OnlineRetail.csv", encoding="ISO-8859-1")

# Quick overview
print("Shape of dataset:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

#describe the dataset
print("\nSummary statistics:")
print(df.describe(include='all'))

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isnull().sum())

#dublicate values
#  Exact duplicates (all columns same)
exact_duplicates = df[df.duplicated()]
print(f"Number of exact duplicate rows: {exact_duplicates.shape[0]}")

#show dublicate rows
print(exact_duplicates.head(5))

#Check if InvoiceNo repeats but products are different
invoice_groups = df.groupby('InvoiceNo')['StockCode'].nunique()
multi_item_invoices = invoice_groups[invoice_groups > 1]
print(f"Invoices with multiple different products: {len(multi_item_invoices)}")
