import pandas as pd
import os

def transform_data(df):
    """
    Cleans and transforms the e-commerce dataset by:
    1. Dropping rows with missing CustomerID.
    2. Converting InvoiceDate to datetime format.
    3. Removing negative or zero quantities.
    """
    # Drop rows with missing CustomerID
    df = df.dropna(subset=['CustomerID'])
    
    # Convert the InvoiceDate to datetime format
    df.loc[:, 'InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M')
    
    # Remove negative or zero quantities
    df = df[df['Quantity'] > 0]
    
    return df

def save_transformed_data(df, output_path):
    """
    Saves the transformed DataFrame as a CSV file.
    Creates the directory if it doesn't exist.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Transformed data saved at: {output_path}")

# File paths
input_file_path = 'data/data.csv'  # Replace with your actual CSV file path
output_file_path = 'data/transformed_data.csv'  # Output file path

# Read raw data
df = pd.read_csv(input_file_path, encoding='ISO-8859-1')

# Transform data
transformed_df = transform_data(df)

# Save transformed data
save_transformed_data(transformed_df, output_file_path)

# Print first 5 rows
print(transformed_df.head())
