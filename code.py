import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Company Monthly Hours Dashboard", layout="wide")

st.title("📊 Company Monthly Hours Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Filter section
    st.sidebar.header("🔍 Filters")
    city_filter = st.sidebar.multiselect("Select City", options=df['City'].unique())
    company_filter = st.sidebar.multiselect("Select Company", options=df['Company'].unique())

    filtered_df = df.copy()
    if city_filter:
        filtered_df = filtered_df[filtered_df['City'].isin(city_filter)]
    if company_filter:
        filtered_df = filtered_df[filtered_df['Company'].isin(company_filter)]

    st.subheader("📑 Filtered Data")
    st.dataframe(filtered_df)

    # Basic Stats
    st.subheader("📈 Monthly Hours Summary")
    st.write(f"Average Monthly Hours: {filtered_df['MonthlyHours'].mean():.2f}")
    st.write(f"Maximum Monthly Hours: {filtered_df['MonthlyHours'].max()}")
    st.write(f"Minimum Monthly Hours: {filtered_df['MonthlyHours'].min()}")

    # Plot
    st.subheader("📉 Monthly Hours by City")
    plt.figure(figsize=(10, 5))
    sns.boxplot(x="City", y="MonthlyHours", data=filtered_df)
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.info("Please upload a CSV or Excel file to begin.")
