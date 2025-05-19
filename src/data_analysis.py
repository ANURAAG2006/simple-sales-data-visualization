import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    # Ensure numeric types for calculations
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['Unit Price'] = pd.to_numeric(df['Unit Price'], errors='coerce')
    df['Total Sales'] = df['Quantity'] * df['Unit Price']
    return df

def get_monthly_sales(df):
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Total Sales'].sum().reset_index()
    monthly_sales['Month'] = monthly_sales['Month'].astype(str)
    return monthly_sales

def top_products(df, n=5):
    product_sales = df.groupby('Product')['Total Sales'].sum().sort_values(ascending=False)
    return product_sales.head(n)
