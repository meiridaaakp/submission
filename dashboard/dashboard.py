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

# Conclusion section
st.subheader("Kesimpulan")
st.write("""
1. Visualisasi menunjukkan bahwa cuaca memiliki dampak yang signifikan terhadap jumlah peminjam sepeda.
2. Terdapat perbedaan jelas antara peminjaman sepeda pada hari kerja dan hari libur.
""")
st.caption('Copyright (c), created by Meirida Karisma Putri')


