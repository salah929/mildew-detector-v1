import streamlit as st

st.set_page_config(page_title="Mildew Detector", page_icon="🍒", layout="wide")

st.title("Mildew Detector in Cherry Leaves 🍒")
st.markdown("Welcome to the Mildew Detector app.")
st.write(
    "This app allows you to explore and detect **mildew infection** "
    "in cherry leaves using **Convolutional Neural Networks (CNNs)**."
)
st.write(
    "You can visualize the dataset, upload your own images for prediction, "
    "and evaluate model performance."
)

# Footer (optional)
st.markdown("---")
st.caption("Developed by Salah Aldien Alsaleh — 2025")
