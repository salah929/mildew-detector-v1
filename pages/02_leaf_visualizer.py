import streamlit as st
import os
from PIL import Image
import random
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.image import imread

st.set_page_config(page_title="Leaf Visualizer", page_icon="🖼️", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center;'>🖼️ Leaf Visualizer</h1>
    <h3 style='text-align: center; color: #555;'>
    Explore and compare healthy and infected leaves</h3>
    """,
    unsafe_allow_html=True)

version = 'v1'
st.markdown("---")

st.header("Difference Between Average and Variability Image")
avg_healthy_path = os.path.join("outputs", version, "avg_var_healthy.png")
avg_infected_path = os.path.join("outputs", version,
                                 "avg_var_powdery_mildew.png")
avg_healthy_img = Image.open(avg_healthy_path)
avg_infected_img = Image.open(avg_infected_path)
st.image(avg_healthy_img, caption="Average Healthy Leaf",
         use_container_width=True)
st.image(avg_infected_img, caption="Average Infected Leaf",
         use_container_width=True)
st.markdown("---")

st.header("Differences Between Average Healthy and Infected Leaves")
avg_diff_img = os.path.join("outputs", version, "avg_diff.png")
diff_between_avgs = Image.open(avg_diff_img)

st.image(diff_between_avgs, caption='Difference between average images')
st.markdown("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # Check if the selected label exists
    if label_to_display in labels:
        label_dir = os.path.join(dir_path, label_to_display)
        images_list = os.listdir(label_dir)

        # Check if montage size is less than or equal to number of images
        if nrows * ncols <= len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            st.warning(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} images in the subset. "
                f"You requested a montage with {nrows * ncols} spaces."
            )
            return

        # Prepare plot indices
        plot_idx = list(itertools.product(range(nrows), range(ncols)))

        # Create the figure
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

        for x in range(nrows * ncols):
            img_path = os.path.join(label_dir, img_idx[x])
            img = imread(img_path)
            img_shape = img.shape

            ax = axes[plot_idx[x][0], plot_idx[x][1]]
            ax.imshow(img)
            ax.set_title(f"{img_shape[1]}px × {img_shape[0]}px")
            ax.set_xticks([])
            ax.set_yticks([])

        plt.tight_layout()
        st.pyplot(fig)

    else:
        st.error(f"The selected label '{label_to_display}' does not exist.")
        st.info(f"Available labels: {labels}")


st.markdown("* ### Image Montage")
my_data_dir = os.path.join("images", "sub_validation_set")
labels = os.listdir(my_data_dir)
label_to_display = st.selectbox(label="Select label",
                                options=labels, index=0)
if st.button("Create Montage"):
    image_montage(
        dir_path=my_data_dir,
        label_to_display=label_to_display,
        nrows=3,
        ncols=3,
        figsize=(10, 10)
    )
