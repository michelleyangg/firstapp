import streamlit as st

# Judul quiz
st.title("🧍‍♀️🧍‍♂️ Apa Tipe Tubuhmu?")

# Menampilkan soal pertama
st.header("1. Bagaimana bentuk tubuhmu saat ini tanpa latihan khusus?")
q1 = st.radio("Pilih satu:", [
    "Sangat kurus dan susah naik berat badan", 
    "Berisi, mudah naik berat badan, tapi susah turun", 
    "Proporsional dan berotot alami"
], key="q1")

# Menampilkan soal kedua
st.header("2. Apa yang terjadi saat kamu mencoba menambah berat badan?")
q2 = st.radio("Pilih satu:", [
    "Sulit sekali, makan banyak pun tetap kurus", 
    "Mudah sekali naik berat badan", 
    "Cukup cepat, tapi tetap seimbang "
], key="q2")

# Menampilkan soal ketiga
st.header("3. Seberapa mudah kamu membentuk otot saat berolahraga?")
q3 = st.radio("Pilih satu:", [
    "Butuh waktu lama dan hasilnya sedikit", 
    "Cukup cepat dan mudah", 
    "Otot terbentuk tapi sering tertutup lemak"
], key="q3")

st.header("4. Bagaimana nafsu makanmu?")
q4 = st.radio("Pilih satu:", [
    "Tidak terlalu besar, kadang harus dipaksa makan", 
    "Sangat besar, sering lapar", 
    " Normal dan stabil"
], key="q4")

st.header("5.  Bagaimana bentuk lengan dan kaki kamu secara umum?")
q5 = st.radio("Pilih satu:", [
    "Panjang dan kecil, tidak banyak massa otot", 
    "Pendek dan besar, cenderung berlemak", 
    "Tegap dan berisi, cenderung berotot "
], key="q5")




# Tombol untuk melihat hasil
if st.button("Lihat Hasil"):
    # Atur skor awal
    skor_ectomorph = 0
    skor_endomorph = 0
    skor_mesomorph = 0
    
    # Hitung skor untuk soal 1
    if q1 == "Sangat kurus dan susah naik berat badan":
        skor_ectomorph = skor_ectomorph + 1
    elif q1 == "Berisi, mudah naik berat badan, tapi susah turun":
        skor_endomorph = skor_endomorph + 1
    else:
        skor_mesomorph = skor_mesomorph + 1
    
    # Hitung skor untuk soal 2
    if q2 == "Sulit sekali, makan banyak pun tetap kurus":
        skor_ectomorph = skor_ectomorph + 1
    elif q2 == "Mudah sekali naik berat badan":
        skor_endomorph = skor_endomorph + 1
    else:
        skor_mesomorph = skor_mesomorph + 1
    
    # Hitung skor untuk soal 3
    if q3 == "Butuh waktu lama dan hasilnya sedikit":
        skor_ectomorph = skor_ectomorph + 1
    elif q3 == "Cukup cepat dan mudah":
        skor_mesomorph = skor_mesomorph + 1
    else:
        skor_endomorph = skor_endomorph + 1
    
     # Hitung skor untuk soal 4
    if q4 == "Tidak terlalu besar, kadang harus dipaksa makan":
        skor_ectomorph = skor_ectomorph + 1
    elif q4 == "Sangat besar, sering lapar":
        skor_endomorph = skor_endomorph + 1
    else:
        skor_mesomorph = skor_mesomorph + 1

    # Hitung skor untuk soal 5
    if q5 == "Tidak terlalu besar, kadang harus dipaksa makan":
        skor_ectomorph = skor_ectomorph + 1
    elif q5 == "Sangat besar, sering lapar":
        skor_endomorph = skor_endomorph + 1
    else:
        skor_mesomorph = skor_mesomorph + 1
    
    # Tampilkan hasil
    st.subheader("🧾 Hasil Kamu:")
    
    # Tentukan hasil berdasarkan skor tertinggi
# Cari skor tertinggi
    hasil = max(skor_mesomorph, skor_ectomorph, skor_endomorph)

# Tampilkan hasil berdasarkan siapa yang punya skor tertinggi
    if hasil == skor_endomorph:
        st.success("Tipe tubuhmu adalah ENDOMORPH! 🍔")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGkyMjI2czB6cnAzNG9jbzJxZzM3bWRkajQzam95NGkxZjhja25yNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4SIS29pDG0CWHUK56L/giphy.gif")
        st.text("Tipe tubuh endomorph cenderung memiliki lemak tubuh yang lebih banyak dan lebih sulit untuk menurunkan berat badan. Biasanya, orang dengan tipe tubuh ini memiliki pinggul yang lebih lebar dan bahu yang lebih sempit. Mereka juga cenderung memiliki otot yang lebih besar dan lebih kuat, tetapi juga lebih banyak lemak tubuh.")
        st.text("Untuk menurunkan berat badan, orang dengan tipe tubuh endomorph perlu melakukan latihan kardiovaskular dan mengatur pola makan yang sehat. Latihan beban juga dapat membantu membangun otot dan meningkatkan metabolisme.")
        st.text("Contoh: Chris Pratt, Adele, dan Kim Kardashian.")
    elif hasil == skor_ectomorph:
        st.success("Tipe tubuhmu adalah ECTOMORPH! 🏃‍♂️")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2NvcTlwczR2b3pqN2hiZ3dmM3RtZGJ4ZjU3ZmludjA4c204NXBpdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ghHDuqJ1uh9vP2gKdC/giphy.gif")
        st.text("Tipe tubuh ectomorph cenderung memiliki tubuh yang ramping dan kurus, dengan sedikit lemak tubuh dan otot. Mereka biasanya memiliki bahu yang sempit, pinggul yang sempit, dan lengan serta kaki yang panjang. Orang dengan tipe tubuh ini cenderung sulit untuk menambah berat badan dan membangun otot.")
        st.text("Untuk membangun otot, orang dengan tipe tubuh ectomorph perlu melakukan latihan beban yang intens dan mengonsumsi makanan yang kaya kalori dan protein. Latihan kardiovaskular sebaiknya dibatasi agar tidak membakar terlalu banyak kalori.")
        st.text("Contoh: Taylor Swift, Ariana Grande, dan Nicole Kidman.")
    else:
        st.success("Tipe tubuhmu adalah MESOMORPH! 💪")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHFzenpsaXR4Znk3azNqZ3dvenQ5NGJ0dXh0YW81NWYxenNhN2p1aCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKVUn7iM8FMEU24/giphy.gif")
        st.text("Tipe tubuh mesomorph cenderung memiliki tubuh yang atletis dan berotot, dengan sedikit lemak tubuh. Mereka biasanya memiliki bahu yang lebar, pinggul yang sempit, dan lengan serta kaki yang berotot. Orang dengan tipe tubuh ini cenderung mudah untuk menambah berat badan dan membangun otot.")
        st.text("Untuk mempertahankan bentuk tubuh yang ideal, orang dengan tipe tubuh mesomorph perlu melakukan latihan beban dan kardiovaskular secara seimbang. Mereka juga perlu mengatur pola makan yang sehat untuk menjaga berat badan.")
        st.text("Contoh: Jennifer Lopez, Chris Hemsworth, dan Dwayne Johnson.")
    
# Tampilkan jika ada kesalahan
    if skor_ectomorph == 0 and skor_endomorph == 0 and skor_mesomorph == 0:
        st.error("Silakan pilih jawaban untuk semua pertanyaan.")
    else:
        st.success("Terima kasih telah mengikuti quiz ini! Semoga informasi ini bermanfaat untukmu.")
        st.text("Jangan lupa untuk berolahraga secara teratur dan menjaga pola makan yang sehat!")
    st.text("Selamat beraktivitas!")

# Tampilkan jangan kosongkan jawaban
    if q1 == "" or q2 == "" or q3 == "" or q4 == "" or q5 == "":
        st.warning("Silakan pilih jawaban untuk semua pertanyaan.")