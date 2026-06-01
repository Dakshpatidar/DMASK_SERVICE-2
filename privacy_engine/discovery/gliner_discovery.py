from gliner import GLiNER


_model = None


def get_model():

    global _model

    if _model is None:

        _model = GLiNER.from_pretrained(
            "urchade/gliner_medium-v2.1"
        )

    return _model


LABELS = [

    "person",

    "organization",

    "company",

    "startup",

    "business",

    "brand",

    "institution",

    "email",

    "phone number",

    "address",

    "bank account",

    "account number"
]


def gliner_discovery(text):

    model = get_model()

    entities = []

    predictions = model.predict_entities(
        text,
        LABELS
    )

    for pred in predictions:

        label = pred["label"].lower()

        value = pred["text"]

        if label == "person":

            mapped = "NAME"

        elif label in [

            "organization",
            "company",
            "startup",
            "business",
            "brand",
            "institution"

        ]:

            mapped = "ORG"

        elif label == "email":

            mapped = "EMAIL"

        elif label == "phone number":

            mapped = "PHONE"

        elif label in [

            "bank account",
            "account number"

        ]:

            mapped = "ACCOUNT"

        else:

            continue

        entities.append({

            "value": value,

            "label": mapped,

            "start": pred["start"],

            "end": pred["end"],

            "source": "GLINER"

        })

    return entities