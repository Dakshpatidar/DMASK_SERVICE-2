# main.py


from privacy_engine.pipeline.discovery_pipeline import discovery_pipeline


# =========================================
# PROCESS TEXT
# =========================================

def process_text(text):

    results = discovery_pipeline(text)

    return {

        "original_text": text,

        "protected_text": results["protected_text"],

        "entities": results["final_entities"],

        "relationships": results["relationships"],

        "replacement_map": results["replacement_map"]
    }


# =========================================
# TEST
# =========================================

if __name__ == "__main__":

    sample_text = """

    My name is Daksh Patidar.

    I work at Infosys.

    My email is daksh32@gmail.com

    My phone number is 9349248294

    My PAN is ABCDE1234F

    """

    output = process_text(sample_text)

    print("\n========== FINAL OUTPUT ==========\n")

    for key, value in output.items():

        print(f"\n{key.upper()}:\n")

        print(value)