# =========================================
# PARTIAL MASK
# =========================================

def partial_mask(value):

    words = value.split()

    masked_words = []

    for word in words:

        if len(word) <= 1:

            masked_words.append("*")

        else:

            masked_words.append(

                word[0]
                +

                "*" * (len(word) - 1)

            )

    return " ".join(masked_words)


# =========================================
# SAFE MASKING ENGINE
# =========================================

def protect_text(text, entities):

    replacement_map = {}

    counters = {

        "EMAIL": 0,

        "PHONE": 0,

        "PAN": 0,

        "AADHAAR": 0,

        "ACCOUNT": 0,

        "IP_ADDRESS": 0,

        "NAME": 0,

        "ORG": 0,

        "LOCATION": 0
    }

    # =====================================
    # SORT BY START DESC
    # =====================================

    entities = sorted(

        entities,

        key=lambda x: x["start"],

        reverse=True
    )

    protected_text = text

    # =====================================
    # ENTITY LOOP
    # =====================================

    for entity in entities:

        value = entity["value"]

        label = entity["label"]

        start = entity["start"]

        end = entity["end"]

        action = entity.get(
            "policy_action",
            "MASK"
        )

        # =================================
        # IGNORE
        # =================================

        if action == "IGNORE":

            continue

        # =================================
        # FUTURE SAFE COUNTERS
        # =================================

        if label not in counters:

            counters[label] = 0

        counters[label] += 1

        # =================================
        # MASK
        # =================================

        if action == "MASK":

            replacement = (

                f"[{label}_{counters[label]}]"

            )

        # =================================
        # TOKENIZE
        # =================================

        elif action == "TOKENIZE":

            replacement = (

                f"[{label}_TOKEN_{counters[label]}]"

            )

        # =================================
        # REDACT
        # =================================

        elif action == "REDACT":

            replacement = (

                f"[REDACTED_{label}]"

            )

        # =================================
        # PARTIAL MASK
        # =================================

        elif action == "PARTIAL_MASK":

            replacement = partial_mask(
                value
            )

        # =================================
        # FALLBACK
        # =================================

        else:

            replacement = (

                f"[{label}]"

            )

        # =================================
        # POSITION-BASED REPLACEMENT
        # =================================

        protected_text = (

            protected_text[:start]

            +

            replacement

            +

            protected_text[end:]

        )

        replacement_map[value] = (
            replacement
        )

    return (

        protected_text,

        replacement_map
    )