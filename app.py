import streamlit as st
import cv2
import numpy as np
from utils.predict import predict_disease
from utils.graph_plotter import generate_graph
from utils.pdf_generator import create_pdf_report

st.set_page_config(page_title="CardioNexa AI", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧠 CardioNexa AI: Cardiovascular Health Predictor</h1>", unsafe_allow_html=True)

# Patient Info
patient_name = st.text_input("👤 Enter Patient Name:")

# Image Upload
uploaded_file = st.file_uploader("🖼️ Upload CT/MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Predict"):
        score, disease = predict_disease(image)
        generate_graph(score)

        st.markdown(f"### 📊 Heart Health Score: `{score}%` 💓")
        st.markdown(f"### ⚠️ Predicted Disease: `{disease}`")

        st.image("graph.png", caption="Health Score Chart")

        pdf_path = create_pdf_report(patient_name, score, disease)
        with open(pdf_path, "rb") as f:
            st.download_button(label="📄 Download PDF Report", data=f, file_name="Cardio_Report.pdf")
