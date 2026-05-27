PRIORITY_ORDER = {
    "AADHAAR": 1,
    "PAN": 2,
    "EMAIL": 3,
    "PHONE": 4,
    "ACCOUNT": 5,
    "ROLLNO": 6,
    "NAME": 7,
    "ORG": 8,
    "LOCATION": 9
}


def classify_entities(entities):

    best_entities = {}

    for entity in entities:

        value = entity["value"]

        label = entity["label"]

        priority = PRIORITY_ORDER.get(label, 999)

        if value not in best_entities:

            best_entities[value] = entity

        else:

            existing_priority = PRIORITY_ORDER.get(
                best_entities[value]["label"],
                999
            )

            if priority < existing_priority:

                best_entities[value] = entity

    return list(best_entities.values())