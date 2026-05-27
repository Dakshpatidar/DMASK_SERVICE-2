import time

from privacy_engine.pipeline.discovery_pipeline import (
    discovery_pipeline
)


# =========================================
# BENCHMARK DATA
# =========================================

samples = [

    """
    My name is Daksh Patidar.
    I work at Infosys.
    My email is daksh32@gmail.com
    My phone number is 9349248294
    """,

    """
    Rahul Sharma joined Microsoft.
    Contact at rahul@gmail.com
    PAN is ABCDE1234F
    """,

    """
    Employee Raj Verma joined OpenAI.
    Aadhaar is 123412341234
    Phone number is 9988776655
    """
]


# =========================================
# BENCHMARK
# =========================================

total_time = 0

for i, sample in enumerate(samples):

    start = time.time()

    result = discovery_pipeline(sample)

    end = time.time()

    latency = end - start

    total_time += latency

    print("\n")
    print("=" * 60)

    print(f"BENCHMARK TEST {i+1}")

    print("=" * 60)

    print(f"\nLatency: {latency:.4f} sec")

    print("\nProtected Text:\n")

    print(result["protected_text"])

average_latency = total_time / len(samples)

print("\n")
print("=" * 60)

print("AVERAGE LATENCY")

print("=" * 60)

print(f"\nAverage Pipeline Time: {average_latency:.4f} sec")