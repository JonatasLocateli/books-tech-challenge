import streamlit as st
import requests

API_URL = "http://localhost:5000/api/v1/books/stats/overview"

st.title("📊 Book API Analytics")

response = requests.get(API_URL).json()

st.metric("Total de Livros", response["total_books"])
st.metric("Preço Médio", response["average_price"])
st.metric("Rating Médio", response["average_rating"])
