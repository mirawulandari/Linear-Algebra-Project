import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Aplikasi Pemrosesan Gambar")
st.write("Unggah gambar untuk diproses.")

# Unggah file gambar
uploaded_file = st.file_uploader("Pilih file gambar", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Membaca dan menampilkan gambar
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar asli", use_column_width=True)

    # Pemrosesan gambar: Ubah ke grayscale
    grayscale_image = image.convert("L")
    st.image(grayscale_image, caption="Gambar grayscale", use_column_width=True)
