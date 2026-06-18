import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("🏢 Company Analytics")

conn = get_connection()

companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

st.dataframe(companies)

st.metric(
    "Total Companies",
    len(companies)
)