import os
import streamlit as st
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

version = 'v1'

st.markdown(
    """
    <h1 style='text-align: center;'>📊 ML Performance</h1>
    <h3 style='text-align: center; color: #555;'>
    Evaluating model accuracy and generalization performance</h3>
    """,
    unsafe_allow_html=True
)
st.write("---")

st.write("### Train, Validation and Test Set: Labels Frequencies")

labels_path = os.path.join("outputs", version, "labels_distribution.png")
labels_distribution = imread(labels_path)
st.image(
    labels_distribution,
    caption="Labels Distribution on Train, Validation and Test Sets"
)
st.write("---")

st.write("### Model History")

col1, col2 = st.columns(2)

with col1:
    acc_path = os.path.join("outputs", version, "model_training_acc.png")
    model_acc = imread(acc_path)
    st.image(model_acc, caption="Model Training Accuracy")

with col2:
    loss_path = os.path.join("outputs", version, "model_training_losses.png")
    model_loss = imread(loss_path)
    st.image(model_loss, caption="Model Training Losses")
st.write("---")

st.write("### Generalised Performance on Test Set")

test_results = load_test_evaluation(version)
col1, col2 = st.columns([1, 1])

with col1:
    st.dataframe(pd.DataFrame(test_results, index=['Loss', 'Accuracy']))
