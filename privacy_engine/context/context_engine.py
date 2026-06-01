#context_engine.py

SAFE_ACTIONS = {

    "building",
    "creating",
    "developing",
    "launching",
    "founded",
    "founding",
    "starting",
    "running",
    "working",
    "joined",
    "joining",
    "employed"
}


def should_mask_org(entity_text, sentence):

    sentence_lower = sentence.lower()

    entity_lower = entity_text.lower()

    for action in SAFE_ACTIONS:

        pattern = f"{action} {entity_lower}"

        if pattern in sentence_lower:

            return True

    return True