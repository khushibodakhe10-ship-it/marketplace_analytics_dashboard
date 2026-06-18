import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import get_connection

st.title("🎓 Student Analytics")

conn = get_connection()

students = pd.read_sql(
    "SELECT * FROM students",
    conn
)

st.dataframe(students)

if "college_name" in students.columns:

    chart = (
        students.groupby("college_name")
        .size()
        .reset_index(name="Students")
    )

    fig = px.bar(
        chart,
        x="college_name",
        y="Students",
        title="Students by College"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )