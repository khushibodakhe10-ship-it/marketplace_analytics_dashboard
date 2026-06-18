import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("📝 Interview Analytics")

conn = get_connection()

interviews = pd.read_sql(
    "SELECT * FROM interviews",
    conn
)

st.dataframe(interviews)

if "result" in interviews.columns:

    chart = (
        interviews.groupby("result")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        chart,
        names="result",
        values="Count",
        title="Interview Results"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )