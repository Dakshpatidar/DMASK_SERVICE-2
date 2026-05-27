# privacy_engine/confidence/confidence_engine.py


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
    # REGEX ENTITIES
    # =====================================

    if source == "REGEX":

        confidence = 0.99

    # =====================================
    # CONTEXT PATTERN
    # =====================================

    elif source == "CONTEXT_PATTERN":

        confidence = 0.90

    # =====================================
    # NER ENTITIES
    # =====================================

    elif source == "NER":

        confidence = 0.75

    # =====================================
    # ENTITY-SPECIFIC BOOST
    # =====================================

    if label in [

        "EMAIL",
        "PHONE",
        "PAN",
        "AADHAAR"
    ]:

        confidence = max(
            confidence,
            0.95
        )

    entity["confidence"] = confidence

    return entity