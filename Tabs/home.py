import streamlit as st
import numpy as np

def calculate_arms(set_point, measurements):
    n = len(set_point)  # Jumlah set point
    arms = np.sqrt(np.sum((set_point - measurements)**2) / n)
    return arms

def app():
    st.title("Halaman Kalkulasi Arms")

    col1, col2 = st.columns(2)

    with col1:
        sett_70 = st.text_input('Input nilai yang terbaca pada setting point 70%')
        sett_75 = st.text_input('Input nilai yang terbaca pada setting point 75%')
        sett_80 = st.text_input('Input nilai yang terbaca pada setting point 80%')
        sett_85 = st.text_input('Input nilai yang terbaca pada setting point 85%')
    with col2:
        sett_90 = st.text_input('Input nilai yang terbaca pada setting point 90%')
        sett_95 = st.text_input('Input nilai yang terbaca pada setting point 95%')
        sett_100 = st.text_input('Input nilai yang terbaca pada setting point 100%')

    # Set point yang tetap
    set_point = np.array([70, 75, 80, 85, 90, 95, 100])

    # Tombol hitung Arms
    if st.button("Hitung Arms"):
        try:
            # Membaca input pengguna dan konversi ke float
            measurements = np.array([
                float(sett_70),
                float(sett_75),
                float(sett_80),
                float(sett_85),
                float(sett_90),
                float(sett_95),
                float(sett_100)
            ])

            # Hitung Arms
            arms_result = calculate_arms(set_point, measurements)

            # Simpan hasil ke session state
            st.session_state['arms'] = arms_result
            st.session_state['measurements'] = measurements.tolist()  # Simpan data input pengguna
            
            # Tampilkan hasil
            st.success(f"Nilai Arms: {arms_result:.3f}")

        except ValueError:
            st.error("Harap masukkan nilai yang valid pada semua input.")
