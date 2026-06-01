# =========================================
# RISK LEVELS
# =========================================

RISK_LEVELS = {

    # =====================================
    # CRITICAL
    # =====================================

    "AADHAAR": (

        "CRITICAL",

        100
    ),

    # =====================================
    # HIGH
    # =====================================

    "PAN": (

        "HIGH",

        85
    ),

    "PHONE": (

        "HIGH",

        80
    ),

    "ACCOUNT": (

        "HIGH",

        90
    ),

    # =====================================
    # MEDIUM
    # =====================================

    "EMAIL": (

        "MEDIUM",

        60
    ),

    "IP_ADDRESS": (

        "MEDIUM",

        50
    ),

    # =====================================
    # LOW
    # =====================================

    "NAME": (

        "LOW",

        30
    ),

    "ORG": (

        "LOW",

        25
    ),

    "LOCATION": (

        "LOW",

        20
    )
}


# =========================================
# ASSIGN RISK SCORES
# =========================================

def assign_risk_scores(entities):

    updated_entities = []

    for entity in entities:

        label = entity["label"]

        risk_level, risk_score = RISK_LEVELS.get(

            label,

            ("LOW", 10)
        )

        entity["risk_level"] = risk_level

        entity["risk_score"] = risk_score

        updated_entities.append(
            entity
        )

    return updated_entities