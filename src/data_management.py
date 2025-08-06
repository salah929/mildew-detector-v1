import os
import base64
from datetime import datetime
import joblib

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle

version = "v1"


def download_dataframe_as_csv(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" '
        f'download="Report {datetime_now}.csv" target="_blank">'
        'Download Report</a>'
    )
    return href


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)


def generate_hypothesis_pdf(file_path):
    """
    Generates a short hypothesis report PDF and includes visual evidence.
    """
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    # Define a custom caption style to avoid KeyError
    styles.add(
        ParagraphStyle(
            name="Caption",
            parent=styles["Normal"],
            fontSize=9,
            leading=10,
            alignment=1,  # center
            textColor="gray"
        )
    )
    flowables = []

    # Title
    flowables.append(
        Paragraph("Project Hypothesis and Validation", styles['Title'])
    )
    flowables.append(Spacer(1, 12))

    # Hypothesis paragraphs
    flowables.append(Paragraph(
        "We hypothesize that cherry leaves infected with powdery mildew "
        "exhibit visible signs, such as white or gray powdery patches, "
        "which differentiate them from healthy leaves.",
        styles['Normal']
    ))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph(
        "Initial visual inspection and image analysis indicate that infected "
        "leaves tend to show lighter and irregular areas, while healthy "
        "leaves exhibit a more uniform green tone. These differences may be "
        "learned by a machine learning model.",
        styles['Normal']
    ))
    flowables.append(Spacer(1, 12))

    flowables.append(Paragraph(
        "However, pixel variability and difference images reveal no sharply "
        "defined patterns, which suggests the model might rely on subtle "
        "features for classification.",
        styles['Normal']
    ))
    flowables.append(Spacer(1, 24))

    # Visual Evidence section
    flowables.append(Paragraph("Visual Evidence", styles['Heading2']))
    flowables.append(Spacer(1, 12))

    image_width = 2.5 * inch

    # Add Average Healthy Leaf image
    healthy_img_path = os.path.join("outputs", version, "avg_var_healthy.png")
    if os.path.exists(healthy_img_path):
        flowables.append(Image(
            healthy_img_path, width=image_width * 2.2,
            height=image_width
        ))
        flowables.append(Paragraph(
            "Average Healthy Leaf", styles['Caption']
        ))
        flowables.append(Spacer(1, 12))

    # Add Average Infected Leaf image
    infected_img_path = os.path.join(
        "outputs", version, "avg_var_powdery_mildew.png"
    )
    if os.path.exists(infected_img_path):
        flowables.append(Image(
            infected_img_path, width=image_width * 2.2,
            height=image_width
        ))
        flowables.append(Paragraph(
            "Average Mildew-Infected Leaf", styles['Caption']
        ))
        flowables.append(Spacer(1, 12))

    # Build PDF
    doc.build(flowables)


def get_pdf_download_link(file_path, label="Download Hypothesis Report (PDF)"):
    """
    Returns an HTML download link for the generated PDF.
    """
    with open(file_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()

    href = (
        f'<a href="data:application/pdf;base64,{b64}" '
        f'download="hypothesis_report.pdf">{label}</a>'
    )
    return href
