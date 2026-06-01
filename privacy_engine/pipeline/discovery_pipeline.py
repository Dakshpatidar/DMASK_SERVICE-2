#discovery_pipeline.py

# =========================================
# DISCOVERY IMPORTS                       
# =========================================

from privacy_engine.discovery.regex_discovery import regex_discovery

from privacy_engine.discovery.ner_discovery import ner_discovery

from privacy_engine.context_understanding.context_analyzer import (
    analyze_context
)
from privacy_engine.context.context_patterns import (
    context_pattern_discovery
)

from privacy_engine.context.org_context_detector import (
    detect_org_from_context
)

from privacy_engine.classification.classification_layer import (
    classify_entities
)
from privacy_engine.entity_resolution.entity_resolver import (
    resolve_entities
)
from privacy_engine.discovery.gliner_discovery import (
    gliner_discovery
)
# =========================================
# VALIDATION IMPORTS
# =========================================

from privacy_engine.validation.entity_validator import (
    validate_entities
)



# =========================================
# CONTEXT IMPORTS
# =========================================

from privacy_engine.context.context_layer import (
    apply_context_rules
)


# =========================================
# CONSENSUS IMPORTS
# =========================================

from privacy_engine.consensus.consensus_engine import (
    apply_consensus
)


# =========================================
# CONFIDENCE IMPORTS
# =========================================

from privacy_engine.confidence.confidence_engine import (
    assign_confidence
)


# =========================================
# RELATIONSHIP IMPORTS
# =========================================

from privacy_engine.relationship.relationship_mapper import (
    map_relationships
)


# =========================================
# RISK IMPORTS
# =========================================

from privacy_engine.risk.risk_scoring import (
    assign_risk_scores
)


# =========================================
# POLICY IMPORTS
# =========================================

from privacy_engine.policy.policy_resolver import (
    apply_policy_rules
)
# =========================================
# AUDIT IMPORTS
# =========================================

from privacy_engine.audit.audit_logger import (
    generate_audit_logs
)


# =========================================
# MASKING IMPORTS
# =========================================

from privacy_engine.masking.masking_engine import (
    protect_text
)


# =========================================
# REMOVE DUPLICATES
# =========================================

def remove_duplicates(entities):

    unique_entities = []

    seen = set()

    for entity in entities:

        key = (
            entity["value"].lower(),
            entity["label"]
        )

        if key not in seen:

            seen.add(key)

            unique_entities.append(entity)

    return unique_entities


# =========================================
# MAIN PIPELINE
# =========================================

def discovery_pipeline(text):

    # =====================================
    # DISCOVERY LAYERS
    # =====================================

    regex_entities = regex_discovery(text)

    ner_entities = ner_discovery(text)

    context_pattern_entities = (
        context_pattern_discovery(text)
    )

    context_org_entities = (
        detect_org_from_context(text)
    )
    gliner_entities = gliner_discovery(
    text
)

    # =====================================
    # COMBINE ALL ENTITIES
    # =====================================

    all_entities = (

    regex_entities

    + ner_entities

    + gliner_entities

    + context_pattern_entities

    + context_org_entities
)

    ## =====================================
# CONTEXT ANALYSIS
# =====================================

    context_info = analyze_context(
        text
)

# =====================================
# ENTITY VALIDATION
# =====================================

    validated_entities = validate_entities(
        all_entities,
        context_info
)

# =====================================
# ENTITY RESOLUTION
# =====================================

    resolved_entities = resolve_entities(
        validated_entities
)   

# =====================================
# REMOVE DUPLICATES
# =====================================

    unique_entities = remove_duplicates(
        resolved_entities
)

    # =====================================
    # CROSS VALIDATION
    # =====================================

    pan_values = set()

    aadhaar_values = set()

    phone_values = set()

    for entity in unique_entities:

        if entity["label"] == "PAN":

            pan_values.add(
                entity["value"]
            )

        elif entity["label"] == "AADHAAR":

            aadhaar_values.add(
                entity["value"]
            )

        elif entity["label"] == "PHONE":

            phone_values.add(
                entity["value"]
            )

    validated_entities = []

    for entity in unique_entities:

        value = entity["value"]

        label = entity["label"]

        # ---------------------------------
        # PAN CONFLICT
        # ---------------------------------

        if value in pan_values and label in [
            "NAME",
            "ORG"
        ]:
            continue

        # ---------------------------------
        # AADHAAR CONFLICT
        # ---------------------------------

        if value in aadhaar_values and label in [
            "NAME",
            "ORG"
        ]:
            continue

        # ---------------------------------
        # PHONE CONFLICT
        # ---------------------------------

        if value in phone_values and label in [
            "NAME",
            "ORG"
        ]:
            continue

        validated_entities.append(entity)

    # =====================================
    # CLASSIFICATION LAYER
    # =====================================

    classified_entities = classify_entities(
        validated_entities
    )

    # =====================================
    # CONTEXT LAYER
    # =====================================

    context_entities = apply_context_rules(

        text,
        classified_entities
    )

    # =====================================
    # CONFIDENCE ENGINE
    # =====================================

    confidence_entities = []

    for entity in context_entities:

        entity = assign_confidence(
            entity
        )

        label = entity["label"]

        confidence = entity["confidence"]

        # ---------------------------------
        # STRICT CONFIDENCE
        # ---------------------------------

        if label in [

            "EMAIL",
            "PHONE",
            "PAN",
            "AADHAAR"
        ]:

            if confidence < 0.60:
                continue

        # ---------------------------------
        # RELAXED CONFIDENCE
        # ---------------------------------

        elif label in [

            "NAME",
            "ORG"
        ]:

            if confidence < 0.35:
                continue

        confidence_entities.append(
            entity
        )

    # =====================================
    # CONSENSUS ENGINE
    # =====================================

    final_entities = apply_consensus(
        confidence_entities
    )

    # =====================================
    # RELATIONSHIP MAPPING
    # =====================================

    relationships = map_relationships(

        text,
        final_entities
    )

    # =====================================
    # RISK SCORING
    # =====================================

    risk_entities = assign_risk_scores(
        final_entities
    )

    # =====================================
    # POLICY ENGINE
    # =====================================

    policy_entities = apply_policy_rules(
        risk_entities
    )
        # =====================================
    # AUDIT LOGGING
    # =====================================

    audit_logs = generate_audit_logs(
        policy_entities
    )
    

    # =====================================
    # MASKING ENGINE
    # =====================================

    protected_text, replacement_map = (

        protect_text(

            text,
            policy_entities
        )
    )

    # =====================================
    # FINAL OUTPUT
    # =====================================

    return {

        "original_text": text,

        "final_entities": policy_entities,

        "relationships": relationships,

        "protected_text": protected_text,

        "replacement_map": replacement_map,

        "audit_logs": audit_logs
    }