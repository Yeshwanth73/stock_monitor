# app.py
import streamlit as st
from StockPrices import get_stock_price

st.title("Stock Monitor app")
name = st.text_input("Enter the stock symbol to get the price")
if name:
    try:
        price = round(get_stock_price(name), 2)
        st.write(f"The stock price for {name} - ${price}")
    except TypeError:
        st.write("Invalid symbol")