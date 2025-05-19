from src.data_analysis import load_data, get_monthly_sales, top_products
from src.visualizations import plot_monthly_sales, plot_top_products, plot_sales_trend
from src.forecasting import prepare_forecasting_data, predict_next_month_sales
from src.visualizations import (
    plot_monthly_sales,
    plot_top_products,
    plot_sales_trend,
    plot_pie_chart,
    plot_sales_heatmap
)


def main():
    print("📊 Advanced Sales Data Visualization System")
    
    df = load_data("data/sales_data.csv")

    print("\n🔹 Monthly Sales:")
    monthly_sales = get_monthly_sales(df)
    print(monthly_sales)

    # Forecasting
    X, y = prepare_forecasting_data(monthly_sales)
    predicted_sales = predict_next_month_sales(X, y)
    print(f"\n📈 Forecast: Predicted Sales for Next Month: ₹{predicted_sales}")

    # Visualizations
    plot_monthly_sales(monthly_sales)
    plot_sales_trend(monthly_sales)

    print("\n🔹 Top Products:")
    product_sales = top_products(df)
    print(product_sales)
    plot_top_products(product_sales)
    plot_top_products(product_sales)
    plot_pie_chart(df)
    plot_sales_heatmap(df)

if __name__ == "__main__":
    main()

