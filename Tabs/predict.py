import streamlit as st
from web_function import predict

def app(df, x, y):
    st.title("Halaman Prediksi")

    # Mengambil data dari session state
    if 'arms' in st.session_state and 'measurements' in st.session_state:
        # Data pengukuran dari page 1
        measurements = st.session_state['measurements']
        arms_result = st.session_state['arms']

        # Menampilkan nilai input dari page 1
        col1, col2 = st.columns(2)

        with col1:
            sett_70 = st.text_input('Nilai yang terbaca pada setting point 70%', value=str(measurements[0]), disabled=True)
            sett_75 = st.text_input('Nilai yang terbaca pada setting point 75%', value=str(measurements[1]), disabled=True)
            sett_80 = st.text_input('Nilai yang terbaca pada setting point 80%', value=str(measurements[2]), disabled=True)
            sett_85 = st.text_input('Nilai yang terbaca pada setting point 85%', value=str(measurements[3]), disabled=True)
        with col2:
            sett_90 = st.text_input('Nilai yang terbaca pada setting point 90%', value=str(measurements[4]), disabled=True)
            sett_95 = st.text_input('Nilai yang terbaca pada setting point 95%', value=str(measurements[5]), disabled=True)
            sett_100 = st.text_input('Nilai yang terbaca pada setting point 100%', value=str(measurements[6]), disabled=True)
            Arms = st.text_input('Nilai Arms', value=f"{arms_result:.3f}", disabled=True)

        # Kumpulan data fitur
        features = [
            measurements[0], measurements[1], measurements[2], measurements[3], 
            measurements[4], measurements[5], measurements[6], arms_result
        ]

        # Tombol untuk prediksi
        if st.button("Prediksi"):
            prediction, score = predict(x, y, features)
            st.info("Prediksi Sukses....")

            # Menampilkan hasil prediksi
            if prediction == 0:
                st.warning("Alat dinyatakan Tidak Akurat karena Arms Lebih dari batas 4%")
            else:
                st.success("Alat dinyatakan Akurat")

            st.write(f"Model yang digunakan memiliki tingkat akurasi {score*100:.2f}%")
    else:
        st.warning("Tidak ada data dari halaman pertama. Harap hitung Arms terlebih dahulu di halaman sebelumnya.")
