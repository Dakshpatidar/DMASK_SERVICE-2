#context_analyzer.py

import spacy

nlp = spacy.load("en_core_web_sm")


ACTION_WORDS = {

    "build",
    "create",
    "develop",
    "launch",
    "found",
    "start",
    "run",
    "work",
    "join"
}


def analyze_context(text):

    doc = nlp(text)

    context_info = []

    for token in doc:

        # =====================================
        # ACTION DETECTION
        # =====================================

        if token.lemma_.lower() in ACTION_WORDS:

            subject = None

            obj = None

            intent = None

            # =====================================
            # SUBJECT
            # =====================================

            for child in token.children:

                if child.dep_ in [

                    "nsubj",
                    "nsubjpass"
                ]:

                    subject = child.text

            # =====================================
            # OBJECT
            # =====================================

            object_span = []

            for child in token.children:

                if child.dep_ in [

                    "dobj",
                    "pobj",
                    "attr",
                    "oprd"
                ]:

                    object_span = list(
                        child.subtree
                    )

                    break

            # =====================================
            # FALLBACK
            # =====================================

            if not object_span:

                token_index = token.i + 1

                remaining_tokens = []

                for t in doc[token_index:]:

                    if t.is_punct:
                        break

                    remaining_tokens.append(
                        t.text
                    )

                if remaining_tokens:

                    obj = " ".join(
                        remaining_tokens
                    )

            else:

                obj = " ".join(

                    token.text

                    for token

                    in object_span
                )

            # =====================================
            # INTENT
            # =====================================

            if token.lemma_.lower() in [

                "build",
                "create",
                "develop",
                "launch",
                "found",
                "start"
            ]:

                intent = "CREATE_ORG"

            elif token.lemma_.lower() in [

                "work",
                "join"
            ]:

                intent = "ASSOCIATE_ORG"

            # =====================================
            # SAVE
            # =====================================

            context_info.append({

                "subject": subject,

                "verb": token.text,

                "object": obj,

                "intent": intent
            })

    return context_info