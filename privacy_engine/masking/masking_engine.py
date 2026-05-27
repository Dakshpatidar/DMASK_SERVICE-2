# masking_engine.py


# =========================================
# PARTIAL MASK FUNCTION
# =========================================

def partial_mask(value):

    words = value.split()

    masked_words = []

    for word in words:

        if len(word) <= 1:

            masked_words.append("*")

        else:

            masked_word = word[0] + "*" * (len(word) - 1)

            masked_words.append(masked_word)

    return " ".join(masked_words)


# =========================================
# MAIN MASKING ENGINE
# =========================================

def protect_text(text, entities):

    protected_text = text

    replacement_map = {}

    counters = {

        "EMAIL": 0,
        "PHONE": 0,
        "PAN": 0,
        "AADHAAR": 0,
        "NAME": 0,
        "ORG": 0
    }

    # =====================================
    # SORT LONGEST FIRST
    # =====================================

    entities = sorted(
        entities,
        key=lambda x: len(x["value"]),
        reverse=True
    )

    # =====================================
    # APPLY MASKING
    # =====================================

    for entity in entities:

        value = entity["value"]

        label = entity["label"]

        action = entity["policy_action"]

        counters[label] += 1

        # ---------------------------------
        # MASK
        # ---------------------------------

        if action == "MASK":

            replacement = f"[{label}_{counters[label]}]"

        # ---------------------------------
        # TOKENIZE
        # ---------------------------------

        elif action == "TOKENIZE":

            replacement = f"[{label}_TOKEN_{counters[label]}]"

        # ---------------------------------
        # REDACT
        # ---------------------------------

        elif action == "REDACT":

            replacement = f"[REDACTED_{label}]"

        # ---------------------------------
        # PARTIAL MASK
        # ---------------------------------

        elif action == "PARTIAL_MASK":

            replacement = partial_mask(value)

        # ---------------------------------
        # DEFAULT
        # ---------------------------------

        else:

            replacement = f"[{label}]"

        # =================================
        # REPLACE TEXT
        # =================================

        protected_text = protected_text.replace(
            value,
            replacement
        )

        replacement_map[value] = replacement

    return protected_text, replacement_map