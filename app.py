import pandas as pd
import numpy as np
import mysql.connector


def create_order_list():
    data = {
        'OrderID': np.arange(1, 6),
        'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Monitor'],
        'Quantity': np.random.randint(1, 10, size=5),
        'Price_per_Unit': np.random.randint(5000, 20000, size=5),
        'CustomerName': ['Ananya', 'Rahul', 'Priya', 'Vikram', 'Sneha'],
    }
    
    order_df = pd.DataFrame(data)
    order_df['Total_Price'] = order_df['Quantity'] * order_df['Price_per_Unit']
 
    conn = mysql.connector.connect(
        host="localhost",
        user="ananya",
        password="StrongPass@123",
        database="OrderListDB"
    )
    cursor = conn.cursor()
   
    for _, row in order_df.iterrows():
        sql = '''
        INSERT INTO orders (OrderID, Product, Quantity, Price_per_Unit, CustomerName, Total_Price)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, tuple(row))
    
    conn.commit()

    cursor.execute("SELECT * FROM orders")
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=['OrderID', 'Product', 'Quantity', 'Price_per_Unit', 'CustomerName', 'Total_Price'])
    print("Data from MySQL table:\n", df)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_order_list()
