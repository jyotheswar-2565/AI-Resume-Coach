import streamlit as st
from agent import analyze_resume
from utils import extract_text_from_pdf

# ------------------------------
# Page Configuration
# ------------------------------

st.set_page_config(
    page_title="AI Resume & Interview Coach",
    page_icon="📄",
    layout="wide"
)

# ------------------------------
# Application Header
# ------------------------------

st.title("📄 AI Resume & Interview Coach")

st.write(
    "Upload your resume and get AI-powered feedback."
)

# ------------------------------
# Resume Upload Section
# ------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ------------------------------
# Process Uploaded Resume
# ------------------------------

if uploaded_file:

    # Show upload success message
    st.success(
        "✅ Resume Uploaded Successfully"
    )

    # ------------------------------
    # Resume Text Extraction
    # ------------------------------

    resume_text = extract_text_from_pdf(
        uploaded_file
    )

    # ------------------------------
    # Display Extracted Resume
    # ------------------------------

    st.subheader(
        "📄 Extracted Resume Content"
    )

    st.text_area(
        "Resume Text",
        value=resume_text,
        height=300
    )

    # ------------------------------
    # Resume Analysis Button
    # ------------------------------

    if st.button(
        "🔍 Analyze Resume"
    ):

        # ------------------------------
        # AI Analysis Processing
        # ------------------------------

        with st.spinner(
            "Analyzing Resume..."
        ):

            result = analyze_resume(
                resume_text
            )

        # ------------------------------
        # Display AI Analysis
        # ------------------------------

        st.subheader(
            "🤖 AI Resume Analysis"
        )

        st.markdown(result)