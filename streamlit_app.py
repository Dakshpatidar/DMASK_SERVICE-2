import streamlit as st

from privacy_engine.pipeline.discovery_pipeline import (
    discovery_pipeline
)

from privacy_engine.document_processing.document_loader import (
    load_document
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Secure AI Privacy Gateway",
    page_icon="🛡️",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("🛡️ Secure AI Privacy Gateway")

st.markdown(
    """
Enterprise Privacy Masking Engine

Detects and protects:

- Emails
- Phone Numbers
- Aadhaar
- PAN
- Names
- Organizations
- IP Addresses
"""
)

# =========================================
# TEXT INPUT
# =========================================

user_input = st.text_area(
    "Enter Text",
    height=250,
    placeholder="""
My name is Daksh Patidar.
I work at Infosys.
My email is daksh32@gmail.com
My phone number is 9349248294
"""
)

# =========================================
# FILE UPLOAD
# =========================================

uploaded_file = st.file_uploader(
    "Upload Document",
    type=[
        "txt",
        "pdf",
        "csv",
        "xlsx"
    ]
)

# =========================================
# LOAD FILE
# =========================================

if uploaded_file:

    try:

        user_input = load_document(
            uploaded_file
        )

        st.success(
            f"Loaded: {uploaded_file.name}"
        )

        with st.expander(
            "Preview Extracted Text"
        ):

            st.text(
                user_input[:5000]
            )

    except Exception as e:

        st.error(str(e))

# =========================================
# PROCESS BUTTON
# =========================================

if st.button("Protect Data"):

    if not user_input.strip():

        st.warning(
            "Please enter text or upload a document."
        )

    else:

        results = discovery_pipeline(
            user_input
        )

        # =================================
        # PROTECTED TEXT
        # =================================

        st.subheader("🔒 Protected Text")

        st.code(
            results["protected_text"],
            language="text"
        )

        # =================================
        # DOWNLOAD MASKED FILE
        # =================================

        st.download_button(
            label="⬇ Download Masked Text",
            data=results["protected_text"],
            file_name="masked_output.txt",
            mime="text/plain"
        )

        # =================================
        # DETECTED ENTITIES
        # =================================

        st.subheader("📌 Detected Entities")

        entities = results["final_entities"]

        if entities:

            for entity in entities:

                st.json(entity)

        else:

            st.success(
                "No sensitive entities detected."
            )

        # =================================
        # RELATIONSHIPS
        # =================================

        st.subheader("🔗 Relationships")

        relationships = results["relationships"]

        if relationships:

            for relation in relationships:

                st.json(relation)

        else:

            st.info(
                "No relationships detected."
            )

        # =================================
        # REPLACEMENT MAP
        # =================================

        st.subheader("🧩 Replacement Map")

        st.json(
            results["replacement_map"]
        )

        # =================================
        # AUDIT LOGS
        # =================================

        st.subheader("📋 Audit Logs")

        st.json(
            results["audit_logs"]
        )