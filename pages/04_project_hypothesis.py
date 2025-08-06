import os
import streamlit as st
from src.data_management import (
    generate_hypothesis_pdf,
    get_pdf_download_link
)

version = "v1"

st.markdown(
    """
    <h1 style='text-align: center;'>💡 Project Hypothesis and Validation</h1>
    <h3 style='text-align: center; color: #555;'>
    Explore visual patterns to distinguish healthy and infected leaves</h3>
    """,
    unsafe_allow_html=True
)
st.write("---")

st.success(
    "* We hypothesize that cherry leaves infected with powdery mildew "
    "exhibit visible signs, such as white or gray powdery patches, which "
    "differentiate them from healthy leaves.\n\n"
    "* Based on initial visual inspection, infected leaves often show "
    "distinct discoloration and texture patterns. These may be leveraged "
    "by computer vision models to distinguish between the two classes.\n\n"
    "* Image Montage and Average Image analysis indicate that mildew-infected "
    "leaves tend to have lighter, irregular areas, while healthy leaves "
    "exhibit a more uniform green coloration.\n\n"
    "* However, Variability Images and Difference between Averages do not "
    "provide strong, clear boundaries, suggesting that model learning may "
    "depend more on subtle pixel-level cues and less on obvious structural "
    "differences."
)
st.write("---")

st.write("### Business Value of Early Mildew Detection")

st.info(
    "**Protecting Cherry Crops:**\n"
    "Powdery mildew is a common fungal disease that can significantly "
    "reduce cherry yield and quality. Early detection enables farmers to "
    "act promptly and prevent the spread of infection.\n\n"

    "**Targeted Intervention:**\n"
    "With early and accurate identification, treatment can be applied "
    "selectively, minimizing the use of fungicides and reducing "
    "environmental impact.\n\n"

    "**Cost Reduction and Sustainability:**\n"
    "Automated detection systems reduce labor costs associated with "
    "manual inspections, improve decision-making, and support sustainable "
    "farming practices through smart resource usage.\n\n"

    "**Scalability and Digital Agriculture:**\n"
    "Machine learning solutions like this can be scaled to other crops "
    "and regions, enabling data-driven agriculture and supporting food "
    "security in a changing climate."
)
st.write("---")

# Checkbox to toggle content
show_images = st.checkbox("Show Visual Evidence (Images)", value=False)

if show_images:
    st.write("#### Visual Evidence")

    col1, col2 = st.columns(2)
    with col1:
        st.image("outputs/v1/avg_var_healthy.png",
                 caption="Average Healthy Leaf")
    with col2:
        st.image("outputs/v1/avg_var_powdery_mildew.png",
                 caption="Average Mildew-Infected Leaf")

    st.markdown(
        "* The average healthy leaf shows a uniform green tone.\n"
        "* The infected leaf average reveals lighter patches, "
        "hinting at mildew-related discoloration.\n"
        "* These visual clues support our hypothesis about pattern "
        "differences."
    )

else:
    st.write("#### Hypothesis Summary")
    st.success(
        "* We hypothesize that cherry leaves infected with powdery mildew "
        "exhibit visible signs, such as white or gray powdery patches, "
        "which differentiate them from healthy leaves.\n\n"
        "* Based on initial visual inspection, infected leaves often show "
        "discoloration and texture changes. These may help the model "
        "classify leaf health.\n\n"
        "* Image Montage and Average Image analysis suggest consistent "
        "differences in brightness and texture between classes.\n\n"
        "* However, Variability Images and Difference between Averages "
        "do not show clearly defined boundaries, so model learning likely "
        "relies on subtle pixel-level features."
    )
st.write("---")

file_path = os.path.join("outputs", version, "hypothesis_report.pdf")
os.makedirs(os.path.dirname(file_path), exist_ok=True)
if not os.path.exists(file_path):
    generate_hypothesis_pdf(file_path)
st.markdown(get_pdf_download_link(file_path), unsafe_allow_html=True)
