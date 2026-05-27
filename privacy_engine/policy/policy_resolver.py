# policy_resolver.py


# =========================================
# POLICY RULES
# =========================================

POLICY_RULES = {

    "EMAIL": "MASK",

    "PHONE": "TOKENIZE",

    "PAN": "MASK",

    "AADHAAR": "REDACT",

    "NAME": "PARTIAL_MASK",

    "ORG": "MASK"
}


# =========================================
# APPLY POLICY RULES
# =========================================

def apply_policy_rules(entities):

    updated_entities = []

    for entity in entities:

        label = entity["label"]

        action = POLICY_RULES.get(
            label,
            "MASK"
        )

        entity["policy_action"] = action

        updated_entities.append(entity)

    return updated_entities