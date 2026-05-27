from privacy_engine.pipeline.discovery_pipeline import (
    discovery_pipeline
)


# =========================================
# ENTERPRISE TEST DATA
# =========================================

test_cases = [

    # =====================================
    # NAME
    # =====================================

    "My name is Daksh Patidar",

    "I am Rahul Sharma",

    "This is Amit Verma",

    "Employee Raj Verma joined company",

    "User Sara Khan logged in",

    # =====================================
    # EMAIL
    # =====================================

    "My email is daksh32@gmail.com",

    "Contact at rahul@gmail.com",

    "Mail is sara@yahoo.com",

    # =====================================
    # PHONE
    # =====================================

    "My phone number is 9349248294",

    "Call me at 9988776655",

    "Reach me at 9876543210",

    # =====================================
    # PAN
    # =====================================

    "My PAN is ABCDE1234F",

    "PAN number is PQRSX6789Z",

    # =====================================
    # AADHAAR
    # =====================================

    "Aadhaar is 123412341234",

    "Aadhaar number is 987654321012",

    # =====================================
    # ORG
    # =====================================

    "I work at Infosys",

    "I work in Google",

    "I work for Microsoft",

    "Employee at OpenAI",

    "Joined TCS",

    "Currently at Wipro",

    "Organization Capgemini",

    "Developer at Tarqai",

    "Engineer at Deloitte",

    "Intern at Amazon",

    # =====================================
    # MIXED
    # =====================================

    """
    My name is Daksh Patidar.
    I work at Infosys.
    My email is daksh32@gmail.com
    My phone number is 9349248294
    """,

    """
    Rahul Sharma works in Microsoft.
    Contact at rahul@gmail.com
    PAN is ABCDE1234F
    """,

    """
    Employee Raj Verma joined OpenAI.
    Aadhaar is 123412341234
    Phone number is 9988776655
    """,

    """
    I am Sara Khan.
    I work for Capgemini.
    Mail is sara@gmail.com
    """
]


# =========================================
# RUN TESTS
# =========================================

for i, text in enumerate(test_cases):

    print("\n")
    print("=" * 60)

    print(f"TEST CASE {i+1}")

    print("=" * 60)

    print("\nINPUT:\n")

    print(text)

    results = discovery_pipeline(text)

    print("\nPROTECTED TEXT:\n")

    print(results["protected_text"])

    print("\nENTITIES:\n")

    for entity in results["final_entities"]:

        print(entity)

    print("\nRELATIONSHIPS:\n")

    for relation in results["relationships"]:

        print(relation)