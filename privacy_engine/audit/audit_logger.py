#audit_loger.py

def generate_audit_logs(entities):

    audit_logs = []

    for entity in entities:

        audit_logs.append({

            "entity": entity["value"],

            "label": entity["label"],

            "source": entity.get(
                "source",
                "UNKNOWN"
            ),

            "confidence": entity.get(
                "confidence",
                0
            ),

            "risk_level": entity.get(
                "risk_level",
                "LOW"
            ),

            "risk_score": entity.get(
                "risk_score",
                0
            ),

            "action": entity.get(
                "policy_action",
                "NONE"
            ),

            "reason": entity.get(
                "validation_reason",
                "STANDARD_DETECTION"
            )
        })

    return audit_logs