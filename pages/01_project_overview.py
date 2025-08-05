import streamlit as st

st.set_page_config(page_title="Project Overview", page_icon="📘", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center;'>📘 Project Overview</h1>
    <h3 style='text-align: center; color: #555;'>Detecting Mildew in Cherry
    Leaves with Deep Learning</h3>
    """,
    unsafe_allow_html=True
)
st.markdown("---")

st.header("Background")
st.write(
    "Mildew is a common fungal disease affecting cherry leaves. "
    "Early detection is crucial to minimize crop damage. "
    "This project uses Convolutional Neural Networks "
    "(CNNs) to classify images of cherry leaves as either "
    "**infected** or **healthy**."
)
st.markdown("---")

st.header("Dataset")
st.write(
    "We use a publicly available dataset of cherry leaf images consisting of "
    "two classes:\n"
    "- **Healthy leaves**\n"
    "- **Leaves with powdery mildew**\n\n"
    "The dataset was preprocessed and split into "
    "training, validation, and test sets."
)
st.image("images/dataset.png")
st.markdown("---")

st.header("What This App Offers")
st.write("""
- 📘 **Overview**: Learn about the project goals and dataset
- 🖼️ **Visualizer**: Explore and compare healthy and infected leaves
- 🔍 **Detector**: Upload your own image for prediction
- 💡 **Hypothesis**: Understand the problem assumptions
- 📊 **Evaluation**: Review model performance metrics
""")
st.markdown("---")

st.header("Business Requirements")
st.write("""
1. The client wants to **visually distinguish** between healthy
   and infected cherry leaves.

2. The client needs a model that can **automatically predict**
   whether a given leaf image is infected with mildew.
""")
