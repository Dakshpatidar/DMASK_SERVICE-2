import pandas as pd

from PyPDF2 import PdfReader


def load_document(uploaded_file):

    filename = uploaded_file.name.lower()

    # =====================================
    # TXT
    # =====================================

    if filename.endswith(".txt"):

        return uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

    # =====================================
    # PDF
    # =====================================

    elif filename.endswith(".pdf"):

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text

    # =====================================
    # CSV
    # =====================================

    elif filename.endswith(".csv"):

        df = pd.read_csv(uploaded_file)

        return df.astype(str).to_string()

    # =====================================
    # XLSX
    # =====================================

    elif (

        filename.endswith(".xlsx")
        or
        filename.endswith(".xls")
    ):

        df = pd.read_excel(uploaded_file)

        return df.astype(str).to_string()

    else:

        raise ValueError(
            "Unsupported file format"
        )