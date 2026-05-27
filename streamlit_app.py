import streamlit as st

from privacy_engine.pipeline.discovery_pipeline import (
    discovery_pipeline
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
"""
)


# =========================================
# INPUT
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
# PROCESS BUTTON
# =========================================

if st.button("Protect Data"):

    if not user_input.strip():

        st.warning("Please enter some text.")

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