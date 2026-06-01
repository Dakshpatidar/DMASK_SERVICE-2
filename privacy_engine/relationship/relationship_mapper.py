def map_relationships(text, entities):

    relationships = []

    names = [
        e for e in entities
        if e["label"] == "NAME"
    ]

    orgs = [
        e for e in entities
        if e["label"] == "ORG"
    ]

    emails = [
        e for e in entities
        if e["label"] == "EMAIL"
    ]

    phones = [
        e for e in entities
        if e["label"] == "PHONE"
    ]

    accounts = [
        e for e in entities
        if e["label"] == "ACCOUNT"
    ]

    # =====================================
    # DETERMINE USER
    # =====================================

    user_name = "USER"

    if names:

        user_name = names[0]["value"]

    # =====================================
    # ORG RELATIONSHIPS
    # =====================================

    for entity in orgs:

        contexts = entity.get(
            "context",
            []
        )

        for ctx in contexts:

            intent = ctx.get(
                "intent"
            )

            subject = ctx.get(
                "subject"
            )

            if subject:

                if subject.lower() in [

                    "i",
                    "me",
                    "my",
                    "myself"

                ]:

                    source = user_name

                else:

                    source = subject

            else:

                source = user_name

            # -----------------------------
            # CREATE ORG
            # -----------------------------

            if intent == "CREATE_ORG":

                relationships.append({

                    "source": source,

                    "relationship": "FOUNDED",

                    "target": entity["value"]
                })

            # -----------------------------
            # WORKS AT
            # -----------------------------

            elif intent == "ASSOCIATE_ORG":

                relationships.append({

                    "source": source,

                    "relationship": "WORKS_AT",

                    "target": entity["value"]
                })

    # =====================================
    # EMAIL RELATIONSHIPS
    # =====================================

    for email in emails:

        relationships.append({

            "source": user_name,

            "relationship": "HAS_EMAIL",

            "target": email["value"]
        })

    # =====================================
    # PHONE RELATIONSHIPS
    # =====================================

    for phone in phones:

        relationships.append({

            "source": user_name,

            "relationship": "HAS_PHONE",

            "target": phone["value"]
        })

    # =====================================
    # ACCOUNT RELATIONSHIPS
    # =====================================

    for account in accounts:

        relationships.append({

            "source": user_name,

            "relationship": "OWNS_ACCOUNT",

            "target": account["value"]
        })

    return relationships