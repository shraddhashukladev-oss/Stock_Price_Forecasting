import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")  # Chart fullscreen जैसा लगे

st.title("Stock Price Forecasting App")

# Read CSV
df = pd.read_csv("stock_details_5_years.csv")

# Convert 'Date' to datetime if available
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

st.subheader("Data Preview")
st.dataframe(df.head())

# Close Price - Matplotlib Line Chart
st.subheader("Close Price Trend (Matplotlib)")
fig1, ax1 = plt.subplots()
ax1.plot(df['Close'], color='blue')
ax1.set_xlabel("Index")
ax1.set_ylabel("Close Price")
ax1.set_title("Close Price Over Time")
st.pyplot(fig1)

# Close Price - Interactive Plotly Line Chart (if 'Date' column exists)
if 'Date' in df.columns:
    st.subheader("Interactive Close Price Chart (Plotly)")
    fig2 = px.line(df, x='Date', y='Close', title='Close Price Over Time (Interactive)')
    st.plotly_chart(fig2, use_container_width=True)

# Volume Chart (if exists)
if 'Volume' in df.columns:
    st.subheader("Volume Traded Over Time")
    fig3 = px.area(df, x='Date' if 'Date' in df.columns else df.index, y='Volume', title='Volume Over Time')
    st.plotly_chart(fig3, use_container_width=True)

# Moving Average (Optional Bonus)
st.subheader("30-Day Moving Average")
df['MA30'] = df['Close'].rolling(window=30).mean()
fig4 = px.line(df, x='Date' if 'Date' in df.columns else df.index, y=['Close', 'MA30'], 
               labels={'value': 'Price'}, title='Close Price vs 30-Day Moving Average')
st.plotly_chart(fig4, use_container_width=True)


