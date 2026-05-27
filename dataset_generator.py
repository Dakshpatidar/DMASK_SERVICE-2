# dataset_generator.py

from faker import Faker
import random
import json

fake = Faker("en_IN")

# =========================================
# HELPERS
# =========================================

ORGS = [
    "Infosys",
    "TCS",
    "Google",
    "Microsoft",
    "OpenAI",
    "Wipro",
    "Amazon",
    "IBM"
]

CHAT_PREFIXES = [
    "hey bro",
    "pls",
    "urgent",
    "contact me",
    "yo",
    "hello",
    "hi",
    ""
]

PAN_PREFIXES = [
    "my pan is",
    "pan no",
    "pan number",
    "pan:",
    ""
]

AADHAAR_PREFIXES = [
    "aadhaar",
    "adhar",
    "aadhaar no",
    "uid",
    ""
]

PHONE_PREFIXES = [
    "call me",
    "ph no",
    "phone",
    "mobile",
    ""
]


# =========================================
# GENERATORS
# =========================================

def generate_email():

    email = fake.email()

    text = f"{random.choice(CHAT_PREFIXES)} my mail is {email}"

    return {
        "text": text,
        "expected_entities": ["EMAIL"]
    }


def generate_phone():

    phone = str(random.randint(6000000000, 9999999999))

    text = f"{random.choice(PHONE_PREFIXES)} {phone}"

    return {
        "text": text,
        "expected_entities": ["PHONE"]
    }


def generate_pan():

    pan = (
        fake.random_uppercase_letter()
        + fake.random_uppercase_letter()
        + fake.random_uppercase_letter()
        + fake.random_uppercase_letter()
        + fake.random_uppercase_letter()
        + str(random.randint(1000, 9999))
        + fake.random_uppercase_letter()
    )

    text = f"{random.choice(PAN_PREFIXES)} {pan}"

    return {
        "text": text,
        "expected_entities": ["PAN"]
    }


def generate_aadhaar():

    aadhaar = str(random.randint(100000000000, 999999999999))

    text = f"{random.choice(AADHAAR_PREFIXES)} {aadhaar}"

    return {
        "text": text,
        "expected_entities": ["AADHAAR"]
    }


def generate_name_org():

    name = fake.name()

    org = random.choice(ORGS)

    patterns = [

        f"{name} works at {org}",

        f"this is {name} from {org}",

        f"{name} joined {org}",

        f"employee {name} from {org}"
    ]

    text = random.choice(patterns)

    return {
        "text": text,
        "expected_entities": ["NAME", "ORG"]
    }


def generate_mixed():

    name = fake.name()

    org = random.choice(ORGS)

    phone = str(random.randint(6000000000, 9999999999))

    email = fake.email()

    text = (
        f"hey this is {name} from {org} "
        f"call me at {phone} "
        f"mail is {email}"
    )

    return {
        "text": text,
        "expected_entities": [
            "NAME",
            "ORG",
            "PHONE",
            "EMAIL"
        ]
    }


# =========================================
# MAIN GENERATOR
# =========================================

def generate_dataset(size=200):

    dataset = []

    generators = [

        generate_email,
        generate_phone,
        generate_pan,
        generate_aadhaar,
        generate_name_org,
        generate_mixed
    ]

    for _ in range(size):

        generator = random.choice(generators)

        sample = generator()

        dataset.append(sample)

    return dataset


# =========================================
# SAVE DATASET
# =========================================

if __name__ == "__main__":

    dataset = generate_dataset(500)

    with open("synthetic_dataset.json", "w") as f:

        json.dump(dataset, f, indent=4)

    print("\n✅ Dataset Generated Successfully")

    print("Total Samples:", len(dataset))

    print("Saved File: synthetic_dataset.json")