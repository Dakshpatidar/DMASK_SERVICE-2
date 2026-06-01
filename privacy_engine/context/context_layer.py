# =========================================
# GENERIC ORGANIZATION WORDS
# =========================================

GENERIC_ORG_WORDS = {

    "company",
    "organization",
    "firm",
    "startup",
    "business",
    "office",
    "industry",
    "corporation"
}


# =========================================
# GENERIC PERSON WORDS
# =========================================

GENERIC_PERSON_WORDS = {

    "user",
    "customer",
    "employee",
    "admin",
    "administrator",
    "manager",
    "client",
    "person",
    "owner",
    "member",
    "guest",
    "staff",
    "worker",
    "developer"
}


# =========================================
# ACTION WORDS
# =========================================

ACTION_WORDS = {

    "building",
    "creating",
    "developing",
    "launching",
    "starting",
    "founded",
    "founding",
    "working",
    "joining",
    "joined"
}


# =========================================
# CONTEXT FILTERING
# =========================================

def apply_context_rules(text, entities):

    refined_entities = []

    for entity in entities:

        value = entity["value"].strip()

        label = entity["label"]

        value_lower = value.lower()

        # =====================================
        # REMOVE GENERIC ORGS
        # =====================================

        if (

            label == "ORG"

            and

            value_lower in GENERIC_ORG_WORDS
        ):

            continue

        # =====================================
        # REMOVE GENERIC NAMES
        # =====================================

        if (

            label == "NAME"

            and

            value_lower in GENERIC_PERSON_WORDS
        ):

            continue

        # =====================================
        # REMOVE ACTION WORD CAPTURES
        # =====================================

        words = value_lower.split()

        if len(words) > 0:

            if words[0] in ACTION_WORDS:

                continue

        # =====================================
        # VERY SMALL ORGS
        # =====================================

        if (

            label == "ORG"

            and

            len(value) < 3
        ):

            continue

        # =====================================
        # VERY SMALL NAMES
        # =====================================

        if (

            label == "NAME"

            and

            len(value) < 3
        ):

            continue

        # =====================================
        # SINGLE WORD NAME FILTER
        # REDUCES GLINER FALSE POSITIVES
        # =====================================

        if (

            label == "NAME"

            and

            len(value.split()) == 1

            and

            value_lower not in {

                "elon",
                "daksh",
                "rohit",
                "john",
                "musk"
            }

        ):

            continue

        refined_entities.append(
            entity
        )

    return refined_entities