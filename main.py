import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("ecommerce_sales.csv")
df = data
# easy to Visualize the Data by using to_string
print(df.to_string(index = False))
print("\n==================================================")
print("            E-COMMERCE SALES ANALYZER               ")
print("===================================================")
# Finding total orders
total_orders = len(df)
print(f"{'Total Orders':<23}:{total_orders}")
# finding total Quantity
total_quantity = df["Quantity"].sum()
print(f"{'Total Quantity':<23}:{total_quantity}")
# finding total revenue
total_revenue = df["Price"].sum()
print(f"{'Total Revenue':<23}:{"₹"}{total_revenue}")
print()
# printing top selling Products
topselling_product = df.groupby("Product")["Quantity"].sum().idxmax()
print(f"{'Top Selling Product':<23}:{topselling_product}")
# Finding Best Category
best_category = df.groupby("Category")["Quantity"].sum().idxmax()
print(f"{'Best Category':<23}:{best_category}")
# printing top Payment Method
toppayment_method = df.groupby("Payment_Method")["Payment_Method"].sum().idxmax()
print(f"{'Top Payment Method':<23}:{toppayment_method}")
# Printing Highest Price Product
topPrice_product = df.groupby("Product")["Price"].sum().idxmax()
print(f"{'Best Price Product':<23}:{topPrice_product}")
# Printing Top Price
top_price = df.loc[df["Price"].idxmax()]
print(f"{'Highest Price':<23}:{"₹"}{top_price["Price"]}")
# printing lowest selling Product
cheapselling_product = df.groupby("Product")["Quantity"].sum().idxmin()
print(f"{'Cheap Selling Product':<23}:{cheapselling_product}")
print()
print("Total number of Sales for Each Product")
# Finding total no.of sales for each product
product_sales = df.groupby("Product")["Quantity"].sum()
for product,sales in product_sales.items():
    print(f"{product:<23}:{sales}")
print()    
print("Revenue for Each Product")
df["Total_price"] = df["Quantity"]*df["Price"]
# finding Each Category Sales
category_sales = df.groupby("Category")["Price"].sum()
for category,price in category_sales.items():
    print(f"{category:<23}:{"₹"}{price}")
print()
print("Paymet Method Analysis")
# Payment Method analysis    
payment_analysis = df.groupby("Payment_Method")["Total_price"].sum()
for payment,sale in payment_analysis.items():
    print(f"{payment:<23}:{"₹"}{sale}")
print()    
print("Number of Sales on different Payment Methods")
# finding payments on different methods    
payment_analysis = df.groupby("Payment_Method")["Payment_Method"].count()
for payment,sale in payment_analysis.items():
    print(f"{payment:<23}:{sale}")    
print()
print("Average Revenue for each month")   
# printing average revenue for each month 
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month_name()
#month_order = ["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
month_avg = df.groupby("Month")["Total_price"].mean()
for month,sal in month_avg.items():
    print(f"{month:<23}:{"₹"}{sal}")
print()    
print("Quantity for each Category")    
# finding category Quantity
category_quantity = df.groupby("Category")["Quantity"].sum()
for category,quantity in category_quantity.items():
    print(f"{category:<23}:{quantity}")
print()
print("Top 5 Best Selling Products") 
# printing top5 Best Products in Sales
top_products = df.groupby("Product")["Quantity"].sum()  
top5_products = top_products.sort_values(ascending=False).head()
print(f"{top5_products}")
print("=================================================")    
plt.bar(category_quantity.index,category_quantity.values,color = ["#9d2cd1","#4b21cc","#2199cc","#21cc8d"])    
plt.xlabel("Category",size = 12)
plt.ylabel("Quantity",size = 12)
plt.title("Categoty VS Quantity",size = 15,color = "black")
plt.xticks(rotation = 20)
plt.show()
plt.plot(month_avg.index,month_avg.values,marker = ".",markersize = 15,mfc = "red",color = "purple")
plt.grid(color = "blue",linestyle = "dotted")
plt.title("Average revenue per every month",size = 16,color = "#59044d")
plt.xlabel("Month",size = 14,color = "#7a093e")
plt.ylabel("Average Revenue",size = 14,color = "#3c097a")
plt.xticks(rotation = 28)
plt.show()
plt.bar(top5_products.index,top5_products.values,color = ["#a19e0e","#b35410","#7710b3","#b310aa","#b3104c"])
plt.xlabel("Product",size = 13)
plt.ylabel("Sales",size = 13)
plt.title("Top 5 Bets Sales",size = 20)
plt.xticks(rotation = 28)
plt.show()
