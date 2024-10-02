import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from matplotlib.gridspec import GridSpec
%matplotlib inline
sns.set(style='dark')

# Load dataset
df_day = pd.read_csv("day.csv")

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
st.write("""
1. Berdasarkan hasil visualisasi data yang telah dilakukan, diperoleh kesimpulan bahwa cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda. Pada cuaca cerah, jumlah penyewaan sepeda cenderung lebih tinggi, baik untuk pengguna non-registered(casual) maupun pengguna registered. Sebaliknya, pada cuaca hujan salju ringan, jumlah penyewaan sepeda menurun drastis. Dengan demikian, Pengguna non-registered(casual) sangat dipengaruhi oleh kondisi cuaca, sementara pengguna registered cenderung lebih konsisten meskipun dalam cuaca buruk.
2. Berdasarkan hasil visualisasi data yang telah dilakukan, diperoleh bahwa penggunaan sepeda pada hari kerja dan hari libur menunjukkan perbedaan pola antara pengguna non-registered(casual) dan pengguna registered. Pengguna non-registered(casual) lebih banyak menyewa sepeda pada hari libur, sedangkan pengguna registered lebih sering menyewa sepeda pada hari kerja. Dengan demikian, jumlah peminjam sepeda paling banyak terjadi pada hari kerja untuk pengguna registered, sedangkan bagi pengguna non-registered(casual), hari libur adalah waktu dengan jumlah penyewaan terbanyak.
""")
st.caption('Copyright (c), created by Meirida Karisma Putri')
