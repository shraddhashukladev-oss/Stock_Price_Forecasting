import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Stock Price Dashboard", layout="wide")

# Custom Page Styling
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .block-container {
            padding: 2rem 1rem;
        }
        h1, h2, h3 {
            text-align: center;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Stock Price Dashboard</h1>", unsafe_allow_html=True)

# Sidebar for File Upload
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Ensure date format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    # Data Preview
    st.subheader("Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Layout Columns
    col1, col2 = st.columns(2)

    # Close Price Chart
    with col1:
        st.subheader("Close Price Over Time")
        fig1 = px.line(df, x='Date' if 'Date' in df.columns else df.index, y='Close',
                       title="Close Price", color_discrete_sequence=['#0066cc'])
        fig1.update_layout(title_x=0.5, plot_bgcolor='white', height=400)
        st.plotly_chart(fig1, use_container_width=True)

    # Volume Chart
    if 'Volume' in df.columns:
        with col2:
            st.subheader("Volume Traded Over Time")
            fig2 = px.area(df, x='Date' if 'Date' in df.columns else df.index, y='Volume',
                           title="Volume Traded", color_discrete_sequence=['#00b894'])
            fig2.update_layout(title_x=0.5, plot_bgcolor='white', height=400)
            st.plotly_chart(fig2, use_container_width=True)

    # Moving Average Chart
    st.subheader("30-Day Moving Average")
    df['MA30'] = df['Close'].rolling(window=30).mean()
    fig3 = px.line(df, x='Date', y=['Close', 'MA30'],
                   labels={'value': 'Price', 'variable': 'Series'},
                   title="Close Price vs 30-Day MA",
                   color_discrete_map={'Close': '#1e90ff', 'MA30': '#a29bfe'})
    fig3.update_layout(title_x=0.5, plot_bgcolor='white', height=500)
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.warning("Please upload a CSV file using the sidebar.")
