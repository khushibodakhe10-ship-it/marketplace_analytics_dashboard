import streamlit as st
import pandas as pd
from db_connection import get_connection

st.set_page_config(
    page_title="Marketplace Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Marketplace Analytics Dashboard")

conn = get_connection()

students = pd.read_sql("SELECT * FROM students", conn)
jobs = pd.read_sql("SELECT * FROM jobs", conn)
companies = pd.read_sql("SELECT * FROM companies", conn)
hires = pd.read_sql("SELECT * FROM hires", conn)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Students", len(students))

with col2:
    st.metric("Jobs", len(jobs))

with col3:
    st.metric("Companies", len(companies))

with col4:
    st.metric("Hires", len(hires))

st.success("Use the sidebar to open analytics pages.")