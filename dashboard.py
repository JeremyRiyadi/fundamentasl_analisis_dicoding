# Import Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df["product_category_name"] = (
        df["product_category_name"]
        .fillna("unknown")
        .astype(str)
    )
    return df

df = load_data()
num_cols = df.select_dtypes(include="number").columns

# Title & Description
st.title("Product Data Analysis Dashboard")
st.write(
    "Dashboard ini menampilkan hasil exploratory data analysis "
    "dan insight bisnis terkait karakteristik produk dan biaya logistik"
)

# Sidebar Filter
st.sidebar.header("Filter Data")

selected_categories = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    sorted(df["product_category_name"].unique())
)

# Apply filter dataframe
filtered_df = df.copy()
if selected_categories:
    filtered_df = filtered_df[
        filtered_df["product_category_name"].isin(selected_categories)
    ]

# Dataset Overview
st.header("Dataset Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Jumlah Produk", len(filtered_df))

with col2:
    st.metric("Jumlah Kategori", filtered_df["product_category_name"].nunique())

with col3:
    st.metric("Jumlah Fitur", filtered_df.shape[1])

# Descriptive Statistics
st.header("Statistik Deskriptif Produk")

selected_col = st.selectbox(
    "Pilih kolom numerikal",
    num_cols
)

st.write(filtered_df[selected_col].describe())

# Visualization 1
st.header("Top 10 Kategori dengan Rata Rata Berat Tertinggi")

top_weight = (
    filtered_df.groupby("product_category_name")["product_weight_g"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig1 = plt.figure(figsize=(10, 5))
plt.bar(top_weight.index, top_weight.values)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Kategori Produk")
plt.ylabel("Rata Rata Berat (gram)")
plt.title("Top 10 Kategori Produk Terberat")
plt.tight_layout()

st.pyplot(fig1)

st.write(
    "Kategori dengan rata rata berat produk tinggi "
    "berpotensi meningkatkan biaya pengiriman dan penyimpanan"
)

# Visualization 2
st.header("Pengaruh Dimensi terhadap Berat Produk")

corr = filtered_df[
    [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
].corr()["product_weight_g"].drop("product_weight_g")

fig2 = plt.figure(figsize=(8, 4))
plt.bar(corr.index, corr.values)
plt.xlabel("Dimensi Produk")
plt.ylabel("Nilai Korelasi")
plt.title("Korelasi Dimensi Produk terhadap Berat")
plt.tight_layout()

st.pyplot(fig2)

st.write(
    "Dimensi dengan korelasi tertinggi terhadap berat "
    "menjadi fokus utama untuk optimasi kemasan dan logistik"
)

# Category Summary
st.header("Ringkasan Berdasarkan Filter")
st.write("Jumlah produk:", len(filtered_df))
st.write("Rata rata berat:", filtered_df["product_weight_g"].mean())
st.write("Rata rata jumlah foto:", filtered_df["product_photos_qty"].mean())

# Conclusion
st.header("Kesimpulan")
st.markdown(
    """
    - Analisis menunjukkan bahwa berat dan dimensi produk sangat dipengaruhi oleh kategori  
    - Filter interaktif membantu eksplorasi karakteristik produk secara spesifik  
    - Optimasi dimensi dan kemasan dapat meminimalkan biaya logistik  
    - Dashboard ini mendukung pengambilan keputusan berbasis data secara dinamis  
    """
)