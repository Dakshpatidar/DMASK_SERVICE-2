#entity_validator.py

def validate_entities(
    entities,
    context_info
):

    validated = []

    detected_objects = set()

    # =====================================
    # CONTEXT OBJECTS
    # =====================================

    for ctx in context_info:

        obj = ctx.get("object")

        if obj:

            detected_objects.add(
                obj.lower().strip()
            )

    # =====================================
    # VALIDATION
    # =====================================

    for entity in entities:

        value = entity["value"]

        label = entity["label"]

        # -------------------------------
        # CONTEXT VERIFIED ORG
        # -------------------------------

        if (

            label == "ORG"

            and

            value.lower().strip()
            in detected_objects
        ):

            entity["validated"] = True

            entity[
                "validation_reason"
            ] = "CONTEXT_VERIFIED"

        validated.append(entity)

    return validated