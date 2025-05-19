import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def prepare_forecasting_data(monthly_sales):
    monthly_sales['Month_Num'] = np.arange(len(monthly_sales))
    X = monthly_sales[['Month_Num']]
    y = monthly_sales['Total Sales']
    return X, y

def predict_next_month_sales(X, y):
    model = LinearRegression()
    model.fit(X, y)
    next_month = pd.DataFrame([[X['Month_Num'].max() + 1]], columns=['Month_Num'])
    prediction = model.predict(next_month)
    return round(prediction[0], 2)
