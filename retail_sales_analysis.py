import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv")

# Display first 5 rows
print(df.head())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Total sales by category
sales = df.groupby("Category")["Sales"].sum()
print(sales)

# Bar Chart
sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.show()
