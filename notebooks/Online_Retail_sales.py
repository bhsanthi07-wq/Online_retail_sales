# Data Analysis

## Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Import Raw Data
df = pd.read_csv("data/Online_Retail_Sales.csv")
print(df)

## Dataset Information
print(df.info())

## Dataset Shape
print(df.shape)

## Check Duplicates
print(df.duplicated().sum())

## Remove Duplicates
print(df.drop_duplicates())

## Check Null Values
print(df.isnull().sum())

## Handle Data
print(df.fillna({'Description': "Unknown"}, inplace=True))
print("Unknown count:", (df['Description'] == "Unknown").sum())


## Remove Null Vales
df = df.dropna(subset=["CustomerID"])
print(df['CustomerID'].isnull().sum())

## Count Unique Values
print(df["CustomerID"].nunique())
print(df["Country"].nunique())
print(df["Description"].unique())

## Convert Datatype
df["CustomerID"]=df["CustomerID"].astype(int)
print(df["CustomerID"])

df["InvoiceDate"]=pd.to_datetime(df["InvoiceDate"])
print(df["InvoiceDate"])

# Basic Information
## Total sales
df["TotalPrice"]=df["Quantity"]*df["UnitPrice"]
print(df["TotalPrice"].sum().astype(int))

## Average sales
print(df["TotalPrice"].mean())

## Total Products
print(df['Description'].value_counts().sum())

## monthly sales
df['Month'] = df['InvoiceDate'].dt.month
df.groupby('Month')['TotalPrice'].sum()


# Data Visualization
## Country Shares
df['Country'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%')
plt.title("Country Shares")
plt.savefig("images/country_shares.png")
plt.show()

## Insight: The United kingdom contributes the highest number of orders compared to other countries.

## Quantity vs UnitPrice
plt.scatter(df['Quantity'], df['UnitPrice'])
plt.xlabel("Quantity")
plt.ylabel("Unit Price")
plt.title("Quantity vs Unit Price")
plt.savefig("images/quantity_vs_unitprice.png")
plt.show()

## Insight: The majority of data points are shows at lower quantity and lower unitprice.

## Top 10 customers
df['CustomerID'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 customers by number of orders")
plt.savefig("images/top 10 customers.png")
plt.show()

## Insight: These top 10 customers are contribute large number of oders.

## Quantity Outliers
sns.boxplot(x=df['Quantity'])
plt.title("Quantity Outliers")
plt.savefig("images/quantity_outliers.png")
plt.show()

## Insight: My dataset contains significant outliers in quantity

## Hours-wise sales
df['Hour'] = df['InvoiceDate'].dt.hour
hourly_sales = df.groupby('Hour')['TotalPrice'].sum()
hourly_sales.plot(kind='bar')
plt.title("Hours-wise Sales")
plt.xlabel("Hours")
plt.ylabel("Total Sales")
plt.savefig("images/hours-wise_sales.png")
plt.show()

## Insight: Sales are concentrated during specific hours of the day.