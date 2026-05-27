# privacy_engine/policy/policy_resolver.py

import json


# =========================================
# LOAD POLICY CONFIG
# =========================================

with open("policy_config.json", "r") as f:

    POLICY_CONFIG = json.load(f)


# =========================================
# APPLY POLICY RULES
# =========================================

def apply_policy_rules(entities):

    updated_entities = []

    for entity in entities:

        label = entity["label"]

        # =================================
        # LOAD CONFIG
        # =================================

        if label in POLICY_CONFIG:

            config = POLICY_CONFIG[label]

            entity["risk_level"] = config[
                "risk_level"
            ]

            entity["risk_score"] = config[
                "risk_score"
            ]

            entity["policy_action"] = config[
                "policy_action"
            ]

        updated_entities.append(entity)

    return updated_entities