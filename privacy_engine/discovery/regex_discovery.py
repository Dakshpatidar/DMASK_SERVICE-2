import re


REGEX_PATTERNS = {

    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    "PHONE": r"\b[6-9]\d{9}\b",

    "AADHAAR": r"\b\d{4}\s?\d{4}\s?\d{4}\b",

    "PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

    "ACCOUNT": r"\b\d{10,18}\b",

    "ROLLNO": r"\b\d{2}[A-Z]{2,5}\d{3,5}\b"
}


def regex_discovery(text):

    entities = []

    for label, pattern in REGEX_PATTERNS.items():

        matches = re.finditer(pattern, text)

        for match in matches:

            entities.append({

                "value": match.group(),

                "label": label,

                "start": match.start(),

                "end": match.end(),

                "source": "REGEX"
            })

    return entities