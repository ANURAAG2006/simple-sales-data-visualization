# Simple Sales Data Visualization

This project is an advanced sales data analysis and visualization system built with Python. It helps you analyze, forecast, and visualize sales data from a CSV file, providing insights into sales trends, top products, and more.

## Features
- **Load and preprocess sales data from CSV**
- **Monthly sales analysis and trend visualization**
- **Sales forecasting for the next month**
- **Top products identification and visualization**
- **Pie chart of product contribution to total sales**
- **Sales heatmap (Product vs Month)**

## Project Structure
```
app.py                  # Main entry point
src/
  data_analysis.py      # Data loading and analysis functions
  forecasting.py        # Sales forecasting logic
  visualizations.py     # All plotting and visualization functions
data/
  sales_data.csv        # Your sales data file
```

## How to Use
1. **Install dependencies**
   - Make sure you have Python 3.x installed.
   - Install required packages:
     ```powershell
     pip install pandas matplotlib seaborn
     ```

2. **Prepare your data**
   - Place your sales data in `data/sales_data.csv`.
   - The CSV should have columns: `Date,Product,Category,Quantity,Unit Price,city,store`

3. **Run the application**
   ```powershell
   python app.py
   ```
   - The program will print analysis results and show visualizations.

## Example Visualizations
- Monthly sales bar chart
- Sales trend line chart
- Top products bar chart
- Product sales pie chart
- Product vs Month sales heatmap

## Customization
- You can use your own sales data by updating `data/sales_data.csv`.
- To generate a large sample dataset, use the provided script in `generated_data/` (if available).

## License
This project is for educational and demonstration purposes.

---
Feel free to fork, modify, and use this project for your own sales data analysis needs!
