import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)

st.markdown(
    """
    <h1 style='text-align: center;'>🔍 Powdery Mildew Detector</h1>
    <h3 style='text-align: center; color: #555;'>
    Detect mildew from leaf image</h3>
    """,
    unsafe_allow_html=True)

st.write("---")

images_buffer = st.file_uploader(
    "Upload cherry leaf images (PNG or JPG). You may select more than one.",
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)

# Handle uploaded images
if images_buffer is not None:
    df_report = pd.DataFrame([])

    for image in images_buffer:
        img_pil = Image.open(image)
        st.info(f"Cherry Leaf Sample: **{image.name}**")

        img_array = np.array(img_pil)
        st.image(
            img_pil,
            caption=(
                f"Image Size: {img_array.shape[1]}px width × "
                f"{img_array.shape[0]}px height"
            )
        )

        version = 'v1'
        resized_img = resize_input_image(img=img_pil, version=version)
        pred_proba, pred_class = load_model_and_predict(
            resized_img, version=version
        )
        plot_predictions_probabilities(pred_proba, pred_class)

        df_report = df_report._append(
            {"Name": image.name, "Result": pred_class}, ignore_index=True
        )
        st.markdown("---")

    if not df_report.empty:
        st.success("Detection Report")
        st.table(df_report)
        st.markdown(download_dataframe_as_csv(df_report),
                    unsafe_allow_html=True)
