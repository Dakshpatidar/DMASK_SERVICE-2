# privacy_engine/context/org_context_detector.py

import re


ORG_CONTEXT_PATTERNS = [

    r"work at ([A-Z][a-zA-Z0-9&_ -]+)",
    r"works at ([A-Z][a-zA-Z0-9&_ -]+)",
    r"working at ([A-Z][a-zA-Z0-9&_ -]+)",

    r"joined ([A-Z][a-zA-Z0-9&_ -]+)",

    r"employee at ([A-Z][a-zA-Z0-9&_ -]+)",
    r"employee of ([A-Z][a-zA-Z0-9&_ -]+)",

    r"from ([A-Z][a-zA-Z0-9&_ -]+)",

    r"company ([A-Z][a-zA-Z0-9&_ -]+)",

    r"organization ([A-Z][a-zA-Z0-9&_ -]+)",

]


def detect_org_from_context(text):

    entities = []

    for pattern in ORG_CONTEXT_PATTERNS:

        matches = re.finditer(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            org = match.group(1).strip()

            entities.append({

                "value": org,

                "label": "ORG",

                "start": match.start(1),

                "end": match.end(1),

                "source": "CONTEXT"

            })

    return entities