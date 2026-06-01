# =========================================
# APPLY CONSENSUS
# =========================================

def apply_consensus(entities):

    final_entities = []

    for entity in entities:

        label = entity["label"]

        confidence = entity.get(
            "confidence",
            0.50
        )

        validated = entity.get(
            "validated",
            False
        )

        # =================================
        # STRICT ENTITIES
        # =================================

        if label in [

            "EMAIL",
            "PHONE",
            "PAN",
            "AADHAAR"
        ]:

            final_entities.append(entity)

            continue

        # =================================
        # CONTEXT VALIDATED
        # =================================

        if validated:

            final_entities.append(entity)

            continue

        # =================================
        # NER / CONTEXT
        # =================================

        if label in [

            "NAME",
            "ORG"
        ]:

            if confidence >= 0.50:

                final_entities.append(
                    entity
                )

            continue

        final_entities.append(
            entity
        )

    return final_entities