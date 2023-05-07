import streamlit as st
from PIL import Image

video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

image = Image.open('animasi.png')

st.image(image, caption='foto')

st.write("---")
left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.image(image, caption='foto')
with middle_column:
    st.write('''Aplikasi Project Logika dan Pemprograman Komputer Kelompok 5:
1. Amanda Berliana Widjaya (2260005)
2. Fifi Nuraini (2260016)
3. Marlina Cahyani (2260027)
4. Putri Nuraini (2260038)
5. Ruri Dwi Arlita (2260049)
6. Afdatul Saputra (2120377)
''')


with right_column:
    st.write('''foto2''')
             
st.write("---")
             
#Perhitungan Konsentrasi Terukur
absorbansi = st.number_input('Masukkan Nilai Absorbansi')
intercep = st.number_input('Masukkan Nilai Intercep')
slope = st.number_input('Masukkan Nilai Slope')

tombol = st.button('Hitung nilai Konsentrasi terukur')

if tombol:
    konsentrasi_terukur = (absorbansi-intercep)/slope
    st.success(f'Nilai Konsentrasi Terukur Adalah {konsentrasi_terukur}')
    
#Perhitungan Kadar 
konsentrasiterukur = st.number_input('Masukkan Nilai Konsentrasi Terukur')
VLT = st.number_input('Masukkan Nilai Volume Labu Takar')
FP = st.number_input('Masukkan Nilai Faktor Pengenceran')
volumesampel = st.number_input('Maukkan Nilai Volume Sampel')


tombol = st.button('Hitung Nilai Kadar')

if tombol:
    kadar = (konsentrasiterukur*VLT*FP)/volumesampel
    st.success(f'Nilai Kadar Adalah {kadar}')
    
#Perhitungan %RPD
nilai_total_kadar = st.number_input('masukkan nilai total kadar')
banyak_jumlah_kadar = st.number_input('masukkan banyak data kadar')

tombol = st.button('Hitung Nilai %RSD')

if tombol:
    RPD = (nilai_total_kadar**1/2)/(nilai_total_kadar/banyak_jumlah_kadar)
    st.success(f'Nilai %RSD adalah {RPD}')
    