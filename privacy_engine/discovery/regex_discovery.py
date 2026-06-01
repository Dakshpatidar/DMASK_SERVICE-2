import re


REGEX_PATTERNS = {

    # =====================================
    # EMAIL
    # =====================================

    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    # =====================================
    # PHONE
    # =====================================

    "PHONE": r"\b[6-9]\d{9}\b",

    # =====================================
    # AADHAAR
    # =====================================

    "AADHAAR": r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    # =====================================
    # PAN
    # =====================================

    "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

    # =====================================
    # ACCOUNT NUMBER
    # =====================================

    "ACCOUNT": r"\b\d{10,18}\b",

    # =====================================
    # ROLL NUMBER
    # =====================================

    "ROLLNO": r"\b\d{2}[A-Z]{2,5}\d{3,5}\b",

    # =====================================
    # IPV4 ADDRESS
    # =====================================

    "IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
}


def regex_discovery(text):

    entities = []

    for label, pattern in REGEX_PATTERNS.items():

        matches = re.finditer(
            pattern,
            text
        )

        for match in matches:

            entities.append({

                "value": match.group(),

                "label": label,

                "start": match.start(),

                "end": match.end(),

                "source": "REGEX"
            })

    return entities