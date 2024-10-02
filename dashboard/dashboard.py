import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

sns.set(style='dark')

# Print the files in the dashboard directory
print("Files in 'dashboard' directory:", os.listdir("dashboard"))

# Load dataset
df_day = pd.read_csv("dashboard/day_data.csv")

# Streamlit configuration
st.set_page_config(page_title="BIKERS", page_icon="🚴‍♂️", layout="wide")

st.markdown("---")
st.title("Bike Sharing Analysis")
st.markdown("---")

# Display dataset
st.subheader("Dataset Jumlah Penyewa Sepeda")
st.dataframe(df_day.head())

# Analysis of weather effect on bike rentals
st.subheader("Pengaruh Cuaca Terhadap Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=df_day, estimator=sum, palette='Set1', ax=ax)
ax.set_title('Pengaruh Cuaca Terhadap Penggunaan Sepeda', fontsize=16)
ax.set_xlabel('Situasi Cuaca', fontsize=12)
ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
st.pyplot(fig)

# Comparison of bike usage on working days vs holidays
st.subheader("Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='cnt', data=df_day, estimator=sum, palette='Set2', ax=ax)
ax.set_title('Perbandingan Penggunaan Sepeda: Hari Kerja vs Hari Libur', fontsize=16)
ax.set_xlabel('Hari Libur vs Hari Kerja', fontsize=12)
ax.set_ylabel('Total Penggunaan Sepeda', fontsize=12)
st.pyplot(fig)

# Conclusion section
st.subheader("Kesimpulan")
st.write("""...""")
st.caption('Copyright (c), created by Meirida Karisma Putri')

