import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Konfigurasi Halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Set Style Visualisasi
sns.set(style='dark')

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df["dteday"] = pd.to_datetime(df["dteday"])
    return df

main_df = load_data()

# --- SIDEBAR  ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Data Filtering")
    
    # Filter Rentang Tanggal
    min_date = main_df["dteday"].min()
    max_date = main_df["dteday"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter Data Berdasarkan Sidebar
df_filtered = main_df[(main_df["dteday"] >= pd.to_datetime(start_date)) & 
                      (main_df["dteday"] <= pd.to_datetime(end_date))]

# --- JUDUL & OVERVIEW ---
st.title('Bike Sharing Data Analysis Dashboard 🚲')

st.subheader('Overview Data')
col1, col2, col3 = st.columns(3)

with col1:
    total_rentals = df_filtered.cnt.sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")

with col2:
    total_casual = df_filtered.casual.sum()
    st.metric("Pengguna Casual", value=f"{total_casual:,}")

with col3:
    total_registered = df_filtered.registered.sum()
    st.metric("Pengguna Registered", value=f"{total_registered:,}")

st.divider()

# --- VISUALISASI 1: PENGARUH SUHU ---
st.markdown("### 1. Pengaruh Kategori Suhu Udara Terhadap Rata-Rata Penyewaan")

temp_order = ['Rendah', 'Sedang', 'Tinggi']
temp_data = df_filtered.groupby('temp_category')['cnt'].mean().reindex(temp_order).reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='temp_category', y='cnt', data=temp_data, palette=['#1E90FF', '#FFC300', '#FF5733'], ax=ax1)
ax1.set_title("Rata-rata Penyewaan Berdasarkan Suhu", fontsize=15, pad=15)
ax1.set_xlabel("Kategori Suhu")
ax1.set_ylabel("Rata-rata Penyewaan Harian")

# Tambahkan label angka di atas bar
for p in ax1.patches:
    ax1.annotate(f'{p.get_height():.0f}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', 
                xytext=(0, 10), textcoords='offset points', fontweight='bold')

st.pyplot(fig1)

with st.expander("Lihat Insight Visualisasi 1"):
    st.write("""
    Suhu udara terbukti memiliki korelasi positif yang sangat kuat terhadap operasional bisnis. Kenaikan suhu berbanding lurus dengan peningkatan jumlah penyewaan harian yang melonjak tajam. Sebaliknya, kondisi suhu rendah (cuaca dingin) merupakan hambatan yang secara konsisten menekan minat penyewaan.
    """)

# --- VISUALISASI 2: HARI KERJA VS LIBUR ---
st.markdown("### 2. Volume Penyewaan: Hari Kerja vs Hari Libur/Akhir Pekan")

day_type_data = df_filtered.groupby('workingday')[['casual', 'registered']].sum().reset_index()
day_melted = day_type_data.melt(id_vars='workingday', var_name='Tipe Pengguna', value_name='Total')

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x='workingday', y='Total', hue='Tipe Pengguna', data=day_melted, palette=['#FF9F43', '#00CFE8'], ax=ax2)
ax2.set_title("Perbandingan Tipe Pengguna pada Hari Kerja & Libur", fontsize=15, pad=15)
ax2.set_xlabel("Kategori Hari")
ax2.set_ylabel("Total Penyewaan")
ax2.ticklabel_format(style='plain', axis='y')
st.pyplot(fig2)

with st.expander("Lihat Insight Visualisasi 2"):
    st.write("""
    Utilitas sepeda bergeser secara signifikan bergantung pada jenis hari. Pada hari kerja, volume penyewaan didominasi secara mutlak oleh pengguna Registered (hampir 2 juta unit) untuk kebutuhan harian seperti bekerja atau sekolah. Namun pada akhir pekan/hari libur, pengguna Casual mencatatkan total penyewaan yang sedikit melampaui akumulasi penyewaan mereka di seluruh hari kerja. Ini menegaskan sensitivitas pengguna Casual terhadap ketersediaan waktu luang.
    """)

st.divider()

# --- REKOMENDASI ---
st.markdown("### **Rekomendasi Action Item:**")
st.info("""
- Tim operasional harus memprioritaskan redistribusi sepeda ke stasiun-stasiun dekat area perumahan dan titik transit pada "Pagi" hari, lalu menggesernya ke area perkantoran pada "Sore" hari untuk melayani pengguna registered. Di sisi lain, sepeda ekstra perlu disiapkan di area taman atau tempat wisata pada "Siang" hari untuk melayani pengguna casual.
- Karena volume penyewaan berada di titik terendah saat suhu "Rendah", periode ini adalah waktu yang paling efisien dan meminimalkan risiko kehilangan revenue untuk menjadwalkan perbaikan massal (maintenance).
- Perusahaan dapat memaksimalkan pendapatan dengan menerapkan strategi penetapan harga dinamis atau bundling. Contohnya, meluncurkan paket diskon "Weekend Explorer" untuk memancing pengguna Casual agar mau mendaftar menjadi member, serta memberikan Voucher Transportasi untuk menjaga retensi pengguna Registered di hari kerja.
""")