import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def app(x, y, df):
    st.title("Halaman Visualisasi Hasil Input dan Kalkulasi")

    # Pastikan data dari page 1 tersedia di session state
    if 'arms' in st.session_state and 'measurements' in st.session_state:
        # Set Point (sumbu x)
        set_points = [70, 75, 80, 85, 90, 95, 100]
        # Data input pengguna (sumbu y)
        measurements = st.session_state['measurements']
        
        # Scatter Plot dengan Garis Regresi
        st.subheader("Scatter Plot Nilai Input vs Set Point")

        # Membuat scatter plot
        fig, ax = plt.subplots()
        sns.scatterplot(x=set_points, y=measurements, color='red', ax=ax)

        # Menghitung regresi linier dari data
        coefficients = np.polyfit(set_points, measurements, 1)  # Linear regression (polynomial degree 1)
        poly_eq = np.poly1d(coefficients)

        # Membuat garis tren (regresi linier)
        trendline = poly_eq(set_points)
        ax.plot(set_points, trendline, color='blue', label=f'Line formula: y = {coefficients[0]:.3f}x + {coefficients[1]:.2f}')
        
        # Menambahkan garis identitas (base case)
        identity_line = set_points  # Karena garis identitas adalah y = x
        ax.plot(set_points, identity_line, color='green', linestyle='--', label="Identity line: y = x")
        
        # Memberikan label dan judul
        ax.set_xlabel("Set Point (%)")
        ax.set_ylabel("Hasil Pengukuran (%)")
        ax.set_title("SpO2 sebagai Fungsi dari Set Point (Dengan Perbandingan Base Case)")
        ax.legend()

        # Menampilkan plot di Streamlit
        st.pyplot(fig)

        ### KALKULASI TAMBAHAN ###
        # Mean Bias
        mean_bias = np.mean(np.array(measurements) - np.array(set_points))

        # Regression Line Slope sudah ada di coefficients[0]

        # Kalkulasi Arms (Root Mean Square Error)
        arms = np.sqrt(np.mean((np.array(measurements) - np.array(set_points)) ** 2))

        # Residual Standard Deviation (s_res)
        residuals = np.array(measurements) - trendline
        s_res = np.sqrt(np.mean(residuals ** 2))

        ### MENAMPILKAN HASIL KALKULASI ###
        st.subheader("Hasil Kalkulasi:")
        st.write(f"**Mean Bias:** {mean_bias:.2f}%")
        st.write(f"**Regression Line Slope:** {coefficients[0]:.3f}")
        st.write(f"**A_rms (Root Mean Square Error):** {arms:.2f}%")
        st.write(f"**s_res (Residual Standard Deviation):** {s_res:.2f}%")
        
        # Menampilkan perbandingan dengan base case
        st.subheader("Perbandingan dengan Base Case:")
        st.write("**Base case**: Regression line fitted to the data falls almost perfectly on the line of identity (slope is 1.00, mean offset is 0).")
        st.write(f"**Garis Regresi Saat Ini**: Slope = {coefficients[0]:.3f}, Mean Bias = {mean_bias:.2f}%")

        st.write("Visualisasi ini menunjukkan perbandingan antara regresi linier dari data input dengan garis identitas (y = x).")
    else:
        st.warning("Tidak ada data dari halaman pertama. Harap lakukan input data terlebih dahulu.")
