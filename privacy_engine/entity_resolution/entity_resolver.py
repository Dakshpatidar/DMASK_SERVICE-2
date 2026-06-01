#entity_resolver.py

# =========================================
# NORMALIZE VALUE
# =========================================

def normalize_value(value):

    return (

        value.lower()
        .strip()
        .replace("-", "")
        .replace("_", "")
    )


# =========================================
# ENTITY RESOLUTION
# =========================================

def resolve_entities(entities):

    resolved = []

    seen = set()

    for entity in entities:

        normalized = normalize_value(
            entity["value"]
        )

        if normalized in seen:

            continue

        seen.add(
            normalized
        )

        resolved.append(
            entity
        )

    return resolved