# context_patterns.py

import re


# =========================================
# PAN PATTERN
# =========================================

PAN_PATTERN = re.compile(
    r'^[A-Z]{5}[0-9]{4}[A-Z]$'
)


# =========================================
# VALIDATE ENTITY
# =========================================

def is_valid_entity(value):

    if not value:
        return False

    words = value.split()

    # avoid garbage captures
    if len(words) > 6:
        return False

    return True


# =========================================
# UNIVERSAL CONTEXT LABELS
# =========================================

CONTEXT_LABELS = {

    # =====================================
    # ORGANIZATION
    # =====================================

    "ORG": [

        r"work at ([A-Z][A-Za-z0-9&_ -]+)",

        r"works at ([A-Z][A-Za-z0-9&_ -]+)",

        r"working at ([A-Z][A-Za-z0-9&_ -]+)",

        r"work in ([A-Z][A-Za-z0-9&_ -]+)",

        r"works in ([A-Z][A-Za-z0-9&_ -]+)",

        r"working in ([A-Z][A-Za-z0-9&_ -]+)",

        r"work for ([A-Z][A-Za-z0-9&_ -]+)",

        r"works for ([A-Z][A-Za-z0-9&_ -]+)",

        r"working for ([A-Z][A-Za-z0-9&_ -]+)",

        r"employee at ([A-Z][A-Za-z0-9&_ -]+)",

        r"employee of ([A-Z][A-Za-z0-9&_ -]+)",

        r"joined ([A-Z][A-Za-z0-9&_ -]+)",

        r"currently at ([A-Z][A-Za-z0-9&_ -]+)",

        r"currently in ([A-Z][A-Za-z0-9&_ -]+)",

        r"company is ([A-Z][A-Za-z0-9&_ -]+)",

        r"organization is ([A-Z][A-Za-z0-9&_ -]+)",

        r"organization ([A-Z][A-Za-z0-9&_ -]+)",

        r"from ([A-Z][A-Za-z0-9&_ -]+)",

        r"consultant at ([A-Z][A-Za-z0-9&_ -]+)",

        r"developer at ([A-Z][A-Za-z0-9&_ -]+)",

        r"engineer at ([A-Z][A-Za-z0-9&_ -]+)",

        r"manager at ([A-Z][A-Za-z0-9&_ -]+)",

        r"intern at ([A-Z][A-Za-z0-9&_ -]+)"
    ],

    # =====================================
    # NAME
    # =====================================

    # =====================================
# NAME
# =====================================

"NAME": [

    r"my name is ([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)",

    r"name is ([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)",

    r"this is ([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)",

    r"([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sjoined",

    r"([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sworks at",

    r"([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sworks in",

    r"([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sworks for",

    r"this is ([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sfrom",

    r"hey this is ([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+)\sfrom"
],

    # =====================================
    # EMAIL
    # =====================================

    "EMAIL": [

        r"email is ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",

        r"mail is ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})",

        r"contact at ([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    ],

    # =====================================
    # PHONE
    # =====================================

    "PHONE": [

        r"phone number is (\d{10})",

        r"mobile number is (\d{10})",

        r"contact number is (\d{10})",

        r"call me at (\d{10})",

        r"reach me at (\d{10})"
    ],

    # =====================================
    # PAN
    # =====================================

    "PAN": [

        r"pan is ([A-Z]{5}[0-9]{4}[A-Z])",

        r"pan number is ([A-Z]{5}[0-9]{4}[A-Z])"
    ],

    # =====================================
    # AADHAAR
    # =====================================

    "AADHAAR": [

        r"aadhaar number is (\d{12})",

        r"aadhaar is (\d{12})"
    ]
}


# =========================================
# CONTEXT DISCOVERY
# =========================================

def context_pattern_discovery(text):

    entities = []

    for label, patterns in CONTEXT_LABELS.items():

        for pattern in patterns:

            matches = re.finditer(

                pattern,
                text,
                re.IGNORECASE
            )

            for match in matches:

                value = match.group(1).strip()

                # =============================
                # IGNORE PAN-LIKE VALUES
                # =============================

                if PAN_PATTERN.match(value):

                    if label != "PAN":

                        continue

                # =============================
                # VALIDATION
                # =============================

                if not is_valid_entity(value):

                    continue

                # =============================
                # BLOCK FALSE POSITIVES
                # =============================

                blocked_values = [

                    "at OpenAI",
                    "at Google",
                    "at Microsoft",
                    "company",
                    "organization"
                ]

                if value in blocked_values:

                    continue

                # =============================
                # ENTITY
                # =============================

                entities.append({

                    "value": value,

                    "label": label,

                    "start": match.start(1),

                    "end": match.end(1),

                    "source": "CONTEXT_PATTERN"
                })

    # =====================================
    # FALLBACK ORGS
    # =====================================

    fallback_orgs = [

        "OpenAI",
        "Infosys",
        "Google",
        "Microsoft",
        "TCS",
        "Wipro",
        "Capgemini",
        "Amazon",
        "Deloitte",
        "Tarqai"
    ]

    for org in fallback_orgs:

        if org.lower() in text.lower():

            already_exists = False

            for entity in entities:

                if (

                    entity["value"].lower()
                    == org.lower()

                    and

                    entity["label"] == "ORG"
                ):

                    already_exists = True

                    break

            if not already_exists:

                entities.append({

                    "value": org,

                    "label": "ORG",

                    "start": text.lower().find(
                        org.lower()
                    ),

                    "end": text.lower().find(
                        org.lower()
                    ) + len(org),

                    "source": "FALLBACK_RULE"
                })

    return entities