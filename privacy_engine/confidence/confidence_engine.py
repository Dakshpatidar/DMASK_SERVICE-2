# =========================================
# ASSIGN CONFIDENCE
# =========================================

def assign_confidence(entity):

    label = entity["label"]

    source = entity.get(
        "source",
        ""
    )

    confidence = 0.50

    # =====================================
    # REGEX
    # =====================================

    if source == "REGEX":

        confidence = 0.99

    # =====================================
    # GLINER
    # =====================================

    elif source == "GLINER":

        confidence = 0.92

    # =====================================
    # CONTEXT VERIFIED
    # =====================================

    elif entity.get(
        "validated",
        False
    ):

        confidence = 0.95

    # =====================================
    # CONTEXT PATTERN
    # =====================================

    elif source == "CONTEXT_PATTERN":

        confidence = 0.90

    # =====================================
    # ORG CONTEXT
    # =====================================

    elif source == "ORG_CONTEXT":

        confidence = 0.85

    # =====================================
    # NER
    # =====================================

    elif source == "NER":

        confidence = 0.75

    # =====================================
    # HIGH SENSITIVITY ENTITIES
    # =====================================

    if label in [

        "EMAIL",

        "PHONE",

        "PAN",

        "AADHAAR",

        "IP_ADDRESS",

        "ACCOUNT"

    ]:

        confidence = max(
            confidence,
            0.95
        )

    # =====================================
    # SAVE CONFIDENCE
    # =====================================

    entity["confidence"] = confidence

    return entity