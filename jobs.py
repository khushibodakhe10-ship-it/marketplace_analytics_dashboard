import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("💼 Job Analytics")

conn = get_connection()

jobs = pd.read_sql(
    "SELECT * FROM jobs",
    conn
)

st.dataframe(jobs)

if "job_category" in jobs.columns:

    chart = (
        jobs.groupby("job_category")
        .size()
        .reset_index(name="Jobs")
    )

    fig = px.pie(
        chart,
        names="job_category",
        values="Jobs",
        title="Jobs by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )