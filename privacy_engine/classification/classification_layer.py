#classification_layer.py
# =========================================
# ENTITY PRIORITY ORDER
# =========================================

PRIORITY_ORDER = {

    "AADHAAR": 1,

    "PAN": 2,

    "EMAIL": 3,

    "PHONE": 4,

    "IP_ADDRESS": 5,

    "ACCOUNT": 6,

    "ROLLNO": 7,

    "NAME": 8,

    "ORG": 9,

    "LOCATION": 10
}


# =========================================
# CLASSIFICATION LAYER
# =========================================

def classify_entities(entities):

    best_entities = {}

    for entity in entities:

        value = entity["value"]

        label = entity["label"]

        priority = PRIORITY_ORDER.get(
            label,
            999
        )

        # =================================
        # FIRST OCCURRENCE
        # =================================

        if value not in best_entities:

            best_entities[value] = entity

        # =================================
        # KEEP HIGHER PRIORITY LABEL
        # =================================

        else:

            existing_priority = PRIORITY_ORDER.get(

                best_entities[value]["label"],

                999
            )

            if priority < existing_priority:

                best_entities[value] = entity

    return list(
        best_entities.values()
    )