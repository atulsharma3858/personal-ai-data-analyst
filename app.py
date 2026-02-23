import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personal AI Data Analyst", layout="wide")

st.title("🤖 Personal AI Data Analyst")
st.write("Upload a CSV file and explore your data interactively.")

uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Info")
    st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if numeric_cols:
        st.subheader("📉 Visualize a Numeric Column")
        col = st.selectbox("Select a column", numeric_cols)

        fig, ax = plt.subplots()
        df[col].hist(bins=20, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)

    st.subheader("💬 Ask a Question (basic)")
    question = st.text_input("Example: What is the average of column X?")

    if question:
        st.info("AI chat coming next — this version focuses on real analysis.")