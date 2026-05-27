# consensus_engine.py


# =========================================
# APPLY CONSENSUS
# =========================================

def apply_consensus(entities):

    grouped = {}

    # =====================================
    # GROUP ENTITIES
    # =====================================

    for entity in entities:

        key = (
            entity["value"],
            entity["label"]
        )

        if key not in grouped:

            grouped[key] = []

        grouped[key].append(entity)

    final_entities = []

    # =====================================
    # SOFT CONSENSUS
    # =====================================

    for key, group in grouped.items():

        entity = group[0]

        label = entity["label"]

        confidence = entity.get(
            "confidence",
            0.50
        )

        source = entity.get(
            "source",
            ""
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
        # NAME / ORG
        # =================================

        if label in [

            "NAME",
            "ORG"
        ]:

            # -----------------------------
            # CONTEXT DETECTION
            # -----------------------------

            if source == "CONTEXT_PATTERN":

                final_entities.append(entity)

                continue

            # -----------------------------
            # NER HIGH CONFIDENCE
            # -----------------------------

            if confidence >= 0.40:

                final_entities.append(entity)

                continue

            # -----------------------------
            # OTHERWISE REJECT
            # -----------------------------

            continue

        # =================================
        # DEFAULT
        # =================================

        final_entities.append(entity)

    return final_entities