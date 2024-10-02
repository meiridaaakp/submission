import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib.gridspec import GridSpec

# Set seaborn style
sns.set(style='dark')

# Load dataset
df_day_new = pd.read_csv("https://raw.githubusercontent.com/meiridaaakp/submission/refs/heads/main/dashboard/day_data")

# Streamlit configuration
st.set_page_config(page_title="BIKERS", page_icon="🚴‍♂️", layout="wide")

st.markdown("---")
st.title("Bike Sharing Analysis")
st.markdown("---")

# Display dataset
st.subheader("Dataset Jumlah Penyewa Sepeda")
st.dataframe(df_day_new.head())

# Visualisasi penyewa sepeda berdasarkan "weathersit"
st.subheader("Jumlah Penyewa Berdasarkan Cuaca")
fig1 = plt.figure(figsize=(12, 10))
gs1 = GridSpec(4, 4, fig1, wspace=0.5, hspace=0.5)
plt.suptitle("Jumlah Penyewa Berdasarkan Cuaca", fontsize=16)

plt.subplot(gs1[:2, 1:3])
sns.boxplot(x='weathersit', y='cnt', data=df_day_new, palette="Set2", hue='weathersit', legend=False)
plt.xlabel("Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewa", fontsize=12)

plt.subplot(gs1[2:, :2])
sns.boxplot(x='weathersit', y='casual', data=df_day_new, palette="Set2", hue='weathersit', legend=False)
plt.xlabel("Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewa Non-Registered (Casual)", fontsize=12)

plt.subplot(gs1[2:, 2:])
sns.boxplot(x='weathersit', y='registered', data=df_day_new, palette="Set2", hue='weathersit', legend=False)
plt.xlabel("Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewa Registered", fontsize=12)

st.pyplot(fig1)

st.subheader("Keterangan")
st.write("""
Berdasarkan hasil visualisasi data di atas, diperoleh bahwa:

a. Jumlah penyewa registered naik pada saat cuaca cerah, dan turun pada saat cuaca hujan salju ringan.
b. Jumlah penyewa non-registered(casual) naik pada saat cuaca cerah dan turun pada saat cuaca hujan salju ringan.
c. Jumlah penyewa registered maupun non-registered(casual) tetap moderat pada cuaca kabut/berawan.

Oleh karena itu, dapat disimpulkan bahwa pada cuaca cerah ("Clear Cuaca") menunjukkan median penyewaan sepeda yang lebih tinggi dibandingkan dengan cuaca berkabut/berawan ("Mist_Cloudy") dan jauh lebih tinggi dibandingkan dengan cuaca hujan salju ringan ("Light_Snow_Rain").
""")
# Visualisasi penyewa sepeda berdasarkan "workingday"
st.subheader("Jumlah Penyewa Berdasarkan Hari Kerja dan Hari Libur")
fig2 = plt.figure(figsize=(13, 10))
gs2 = GridSpec(4, 4, fig2, wspace=0.5, hspace=0.5)
plt.suptitle("Jumlah Penyewa berdasarkan Hari Kerja dan Hari Libur", fontsize=16)

plt.subplot(gs2[:2, 1:3])
sns.boxplot(x='workingday', y='cnt', data=df_day_new, palette="rocket", hue='workingday', legend=False)
plt.xlabel("Hari Kerja (1) vs Hari Libur (0)", fontsize=12)
plt.ylabel("Jumlah Penyewa", fontsize=12)

plt.subplot(gs2[2:, :2])
sns.boxplot(x='workingday', y='casual', data=df_day_new, palette="rocket", hue='workingday', legend=False)
plt.xlabel("Hari Kerja (1) vs Hari Libur (0)", fontsize=12)
plt.ylabel("Jumlah Penyewa Non-Registered (Casual)", fontsize=12)

plt.subplot(gs2[2:, 2:])
sns.boxplot(x='workingday', y='registered', data=df_day_new, palette="rocket", hue='workingday', legend=False)
plt.xlabel("Hari Kerja (1) vs Hari Libur (0)", fontsize=12)
plt.ylabel("Jumlah Penyewa Registered", fontsize=12)

st.pyplot(fig2)
st.subheader("Kesimpulan")
st.write("""
Berdasarkan hasil visualisasi data di atas, diperoleh bahwa:

a. Jumlah penyewa non-registered memiliki total penyewa lebih tinggi pada hari libur
b. jumlah penyewa registered memiliki total penyewa lebih tinggi pada hari kerja

Oleh karena, dapat disimpulkan bahwa jumlah penyewaan sepeda pada hari kerja dan hari libur relatif seimbang, meskipun hari kerja memiliki median yang sedikit lebih tinggi.
""")

# Conclusion section
st.subheader("Kesimpulan")
st.write("""
1. Berdasarkan hasil visualisasi data yang telah dilakukan, diperoleh kesimpulan bahwa cuaca memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda. Pada cuaca cerah, jumlah penyewaan sepeda cenderung lebih tinggi, baik untuk pengguna non-registered(casual) maupun pengguna registered. Sebaliknya, pada cuaca hujan salju ringan, jumlah penyewaan sepeda menurun drastis. Dengan demikian, Pengguna non-registered(casual) sangat dipengaruhi oleh kondisi cuaca, sementara pengguna registered cenderung lebih konsisten meskipun dalam cuaca buruk.
2. Berdasarkan hasil visualisasi data yang telah dilakukan, diperoleh bahwa penggunaan sepeda pada hari kerja dan hari libur menunjukkan perbedaan pola antara pengguna non-registered(casual) dan pengguna registered. Pengguna non-registered(casual) lebih banyak menyewa sepeda pada hari libur, sedangkan pengguna registered lebih sering menyewa sepeda pada hari kerja. Dengan demikian, jumlah peminjam sepeda paling banyak terjadi pada hari kerja untuk pengguna registered, sedangkan bagi pengguna non-registered(casual), hari libur adalah waktu dengan jumlah penyewaan terbanyak.
""")
st.caption('Copyright (c), created by Meirida Karisma Putri')


