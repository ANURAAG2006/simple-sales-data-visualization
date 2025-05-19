import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set a beautiful theme
sns.set_theme(style="whitegrid", palette="pastel")
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 6)

def plot_monthly_sales(monthly_sales):
    plt.figure()
    bar = sns.barplot(x='Month', y='Total Sales', data=monthly_sales)
    plt.title('Monthly Sales Overview', fontsize=16)
    plt.xticks(rotation=45)
    for p in bar.patches:
        bar.annotate(f"₹{int(p.get_height())}", (p.get_x() + 0.3, p.get_height() + 500), fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_top_products(product_sales):
    plt.figure()
    bar = sns.barplot(x=product_sales.values, y=product_sales.index)
    plt.title('Top Selling Products', fontsize=16)
    for i, v in enumerate(product_sales.values):
        plt.text(v + 300, i, f"₹{v}", va='center')
    plt.tight_layout()
    plt.show()

def plot_sales_trend(monthly_sales):
    plt.figure()
    line = sns.lineplot(x='Month', y='Total Sales', data=monthly_sales, marker='o', linewidth=3)
    plt.title('Sales Trend Over Time', fontsize=16)
    plt.xticks(rotation=45)
    for x, y in zip(monthly_sales['Month'], monthly_sales['Total Sales']):
        plt.text(x, y + 2000, f"₹{y}", ha='center')
    plt.tight_layout()
    plt.show()

def plot_pie_chart(df):
    product_sales = df.groupby('Product')['Total Sales'].sum()
    plt.figure(figsize=(9,9))
    plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=140, shadow=True, colors=sns.color_palette('Set2'))
    plt.title("Product Contribution to Total Sales", fontsize=15)
    plt.tight_layout()
    plt.show()

def plot_sales_heatmap(df):
    pivot_table = df.pivot_table(index='Product', columns='Month', values='Total Sales', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlOrBr')
    plt.title('Sales Intensity Heatmap (Product vs Month)', fontsize=16)
    plt.tight_layout()
    plt.show()
