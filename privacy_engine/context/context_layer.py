# context_layer.py

GENERIC_ORG_WORDS = {

    "company",
    "organization",
    "firm",
    "startup",
    "business",
    "office",
    "industry"
}


def apply_context_rules(text, entities):

    refined_entities = []

    for entity in entities:

        value = entity["value"].strip()

        label = entity["label"]

        # =====================================
        # REMOVE GENERIC ORG WORDS
        # =====================================

        if (

            label == "ORG"

            and

            value.lower() in GENERIC_ORG_WORDS
        ):

            continue

        # =====================================
        # REMOVE VERY SMALL NAMES
        # =====================================

        if (

            label == "NAME"

            and

            len(value.split()) < 2
        ):

            continue

        refined_entities.append(entity)

    return refined_entities