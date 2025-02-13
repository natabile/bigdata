import psycopg2
import pandas as pd
from transform import transform_data  # Ensure transform is imported

# Database connection details
DATABASE_URL = "postgresql://postgres:nata2809@localhost/ecommerce_db"  # Modify with actual credentials

# Function to insert data into the transactions table
def insert_data(df):
    # Connect to the PostgreSQL database
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cursor:
            for _, row in df.iterrows():
                print(f"Inserting row with InvoiceNo: {row['InvoiceNo']}")  # Debugging line
                cursor.execute("""
                    INSERT INTO transactions (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    row['InvoiceNo'], row['StockCode'], row['Description'], row['Quantity'],
                    row['InvoiceDate'], row['UnitPrice'], row['CustomerID'], row['Country']
                ))
            conn.commit()
            print("Data inserted successfully into the transactions table.")

# Load the transformed data
file_path = 'data/data.csv'  # Path to the transformed CSV
df = pd.read_csv(file_path, encoding='ISO-8859-1')
transformed_df = transform_data(df)

# Insert the data into the database
insert_data(transformed_df)
