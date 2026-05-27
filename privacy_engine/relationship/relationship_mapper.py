RELATIONSHIP_PATTERNS = {

    "works at": "WORKS_AT",

    "employee at": "WORKS_AT",

    "owns": "OWNS",

    "account number": "HAS_ACCOUNT",

    "email is": "HAS_EMAIL",

    "phone number": "HAS_PHONE"
}


def map_relationships(text, entities):

    relationships = []

    lower_text = text.lower()

    names = [
        e for e in entities
        if e["label"] == "NAME"
    ]

    orgs = [
        e for e in entities
        if e["label"] == "ORG"
    ]

    accounts = [
        e for e in entities
        if e["label"] == "ACCOUNT"
    ]

    emails = [
        e for e in entities
        if e["label"] == "EMAIL"
    ]

    phones = [
        e for e in entities
        if e["label"] == "PHONE"
    ]

    # NAME → ORG

    if "works at" in lower_text:

        for name in names:

            for org in orgs:

                relationships.append({
                    "source": name["value"],
                    "relationship": "WORKS_AT",
                    "target": org["value"]
                })

    # NAME → ACCOUNT

    if "account number" in lower_text:

        for name in names:

            for acc in accounts:

                relationships.append({
                    "source": name["value"],
                    "relationship": "HAS_ACCOUNT",
                    "target": acc["value"]
                })

    # NAME → EMAIL

    if "email" in lower_text:

        for name in names:

            for email in emails:

                relationships.append({
                    "source": name["value"],
                    "relationship": "HAS_EMAIL",
                    "target": email["value"]
                })

    # NAME → PHONE

    if "phone number" in lower_text:

        for name in names:

            for phone in phones:

                relationships.append({
                    "source": name["value"],
                    "relationship": "HAS_PHONE",
                    "target": phone["value"]
                })

    return relationships