# ner_discovery.py

import spacy
import re

nlp = spacy.load("en_core_web_sm")


# =========================================
# PAN PATTERN
# =========================================

PAN_PATTERN = re.compile(
    r'^[A-Z]{5}[0-9]{4}[A-Z]$'
)


# =========================================
# IGNORE WORDS
# =========================================

IGNORE_WORDS = {

    "PAN",
    "AADHAAR",
    "EMAIL",
    "PHONE",
    "ACCOUNT",
    "NUMBER"
}


# =========================================
# NER DISCOVERY
# =========================================

def ner_discovery(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        value = ent.text.strip()

        label = ent.label_

        # =====================================
        # IGNORE PAN-LIKE TOKENS
        # =====================================

        if PAN_PATTERN.match(value):

            continue

        # =====================================
        # IGNORE GARBAGE WORDS
        # =====================================

        if value.upper() in IGNORE_WORDS:

            continue

        # =====================================
        # PERSON -> NAME
        # =====================================

        if label == "PERSON":

            entities.append({

                "value": value,

                "label": "NAME",

                "start": ent.start_char,

                "end": ent.end_char,

                "source": "NER"
            })

        # =====================================
        # ORG -> ORGANIZATION
        # =====================================

        elif label == "ORG":

            entities.append({

                "value": value,

                "label": "ORG",

                "start": ent.start_char,

                "end": ent.end_char,

                "source": "NER"
            })

    return entities