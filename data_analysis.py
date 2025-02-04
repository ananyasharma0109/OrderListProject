import pandas as pd
import numpy as np
import mysql.connector

def create_order_list():
    conn = mysql.connector.connect(
        host="localhost",
        user="ananya",
        password="StrongPass@123", 
        database="OrderListDB"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()

    df = pd.DataFrame(result, columns=['OrderID', 'Product', 'Quantity', 'Price_per_Unit', 'CustomerName', 'Total_Price'])

    print("\nData from MySQL table:\n", df)
    print("\nTotal Sales Revenue:", df['Total_Price'].sum())
    print("\nProduct-wise Sales Data:\n", df.groupby('Product')['Total_Price'].sum())
    print("\nTop Customer(s):\n", df.groupby('CustomerName')['Total_Price'].sum().nlargest(1))

    df.to_excel("OrderList_Analysis.xlsx", index=False)
    print("\nData has been successfully exported to OrderList_Analysis.xlsx")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_order_list()
