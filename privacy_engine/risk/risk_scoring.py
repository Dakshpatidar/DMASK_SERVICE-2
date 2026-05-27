# risk_scoring.py


# =========================================
# RISK LEVELS
# =========================================

RISK_LEVELS = {

    "EMAIL": ("MEDIUM", 60),

    "PHONE": ("HIGH", 80),

    "PAN": ("HIGH", 85),

    "AADHAAR": ("CRITICAL", 100),

    "NAME": ("LOW", 30),

    "ORG": ("LOW", 25)
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

        updated_entities.append(entity)

    return updated_entities