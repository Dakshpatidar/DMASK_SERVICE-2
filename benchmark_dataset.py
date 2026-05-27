benchmark_data = [

    # ==========================
    # EMAIL
    # ==========================

    {
        "text": "My email is daksh32@gmail.com",
        "expected_entities": ["EMAIL"]
    },

    {
        "text": "Contact me at rahul@gmail.com",
        "expected_entities": ["EMAIL"]
    },

    # ==========================
    # PHONE
    # ==========================

    {
        "text": "My phone number is 9349248294",
        "expected_entities": ["PHONE"]
    },

    {
        "text": "Call me at 9876543210",
        "expected_entities": ["PHONE"]
    },

    # ==========================
    # AADHAAR
    # ==========================

    {
        "text": "My Aadhaar number is 800320096721",
        "expected_entities": ["AADHAAR"]
    },

    {
        "text": "Aadhaar: 987654321012",
        "expected_entities": ["AADHAAR"]
    },

    # ==========================
    # PAN
    # ==========================

    {
        "text": "My PAN is ABCDE1234F",
        "expected_entities": ["PAN"]
    },

    {
        "text": "PAN Number: PQRSX6789Z",
        "expected_entities": ["PAN"]
    },

    # ==========================
    # NAME
    # ==========================

    {
        "text": "My name is Daksh Patidar",
        "expected_entities": ["NAME"]
    },

    {
        "text": "I am Rahul Sharma",
        "expected_entities": ["NAME"]
    },

    # ==========================
    # ORG
    # ==========================

    {
        "text": "I work at Infosys",
        "expected_entities": ["ORG"]
    },

    {
        "text": "She joined Google last year",
        "expected_entities": ["ORG"]
    },

    # ==========================
    # MIXED ENTITIES
    # ==========================

    {
        "text": "My name is Daksh Patidar and my email is daksh32@gmail.com",
        "expected_entities": ["NAME", "EMAIL"]
    },

    {
        "text": "I work at Infosys and my phone number is 9349248294",
        "expected_entities": ["ORG", "PHONE"]
    },

    {
        "text": "Rahul Sharma works at TCS. Contact: rahul@gmail.com",
        "expected_entities": ["NAME", "ORG", "EMAIL"]
    },

    {
        "text": "Employee PAN is ABCDE1234F and Aadhaar is 800320096721",
        "expected_entities": ["PAN", "AADHAAR"]
    },

    # ==========================
    # FALSE POSITIVE TESTS
    # ==========================

    {
        "text": "I am learning AI and ML",
        "expected_entities": []
    },

    {
        "text": "Python is used in machine learning",
        "expected_entities": []
    },

    {
        "text": "LLM models are powerful",
        "expected_entities": []
    },

    # ==========================
    # HARD CASES
    # ==========================

    {
        "text": "This is Amit from Microsoft and my number is 9988776655",
        "expected_entities": ["NAME", "ORG", "PHONE"]
    },

    {
        "text": "Contact employee Raj Verma at raj@gmail.com",
        "expected_entities": ["NAME", "EMAIL"]
    },

    {
        "text": "Organization OpenAI hired Rahul Sharma",
        "expected_entities": ["ORG", "NAME"]
    },

    {
        "text": "User Aadhaar is 123412341234 and PAN is ZXCVB1234K",
        "expected_entities": ["AADHAAR", "PAN"]
    },

]