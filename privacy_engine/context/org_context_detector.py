#org_context_detector.py
import re

from privacy_engine.context_understanding.context_analyzer import (
    analyze_context
)

ORG_CONTEXT_PATTERNS = [

    r"work\s+at\s+([^\.,\n]+)",
    r"works\s+at\s+([^\.,\n]+)",
    r"working\s+at\s+([^\.,\n]+)",

    r"work\s+for\s+([^\.,\n]+)",
    r"works\s+for\s+([^\.,\n]+)",

    r"joined\s+([^\.,\n]+)",

    r"employee\s+at\s+([^\.,\n]+)",

    r"building\s+([^\.,\n]+)",
    r"creating\s+([^\.,\n]+)",
    r"developing\s+([^\.,\n]+)",
    r"launching\s+([^\.,\n]+)",
    r"starting\s+([^\.,\n]+)",
    r"founded\s+([^\.,\n]+)",
    r"founding\s+([^\.,\n]+)",
    r"created\s+([^\.,\n]+)",
    r"built\s+([^\.,\n]+)"
]

def detect_org_from_context(text):

    context_info = analyze_context(text)

    entities = []

    for pattern in ORG_CONTEXT_PATTERNS:

        matches = re.finditer(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            org = match.group(1).strip()

            entities.append({

                "value": org,

                "label": "ORG",

                "start": match.start(1),

                "end": match.end(1),

                "source": "ORG_CONTEXT",

                "context": context_info

            })

    return entities