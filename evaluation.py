# evaluation.py

from benchmark_dataset import benchmark_data

from privacy_engine.pipeline.discovery_pipeline import discovery_pipeline


def evaluate():

    total_expected = 0
    total_detected = 0
    total_correct = 0

    print("\n========== EVALUATION STARTED ==========\n")

    for index, sample in enumerate(benchmark_data):

        text = sample["text"]

        expected = sample["expected_entities"]

        results = discovery_pipeline(text)

        detected_labels = []

        for entity in results["final_entities"]:

            detected_labels.append(entity["label"])

        detected_set = set(detected_labels)

        expected_set = set(expected)

        correct = detected_set.intersection(expected_set)

        total_expected += len(expected_set)

        total_detected += len(detected_set)

        total_correct += len(correct)

        print(f"\n----- SAMPLE {index + 1} -----")

        print("TEXT:")
        print(text)

        print("\nEXPECTED:")
        print(expected_set)

        print("\nDETECTED:")
        print(detected_set)

        print("\nCORRECT:")
        print(correct)

    # ==========================
    # METRICS
    # ==========================

    precision = 0
    recall = 0
    f1_score = 0

    if total_detected > 0:
        precision = total_correct / total_detected

    if total_expected > 0:
        recall = total_correct / total_expected

    if precision + recall > 0:
        f1_score = 2 * ((precision * recall) / (precision + recall))

    # ==========================
    # FINAL RESULTS
    # ==========================

    print("\n\n========== FINAL METRICS ==========\n")

    print(f"Total Expected Entities : {total_expected}")

    print(f"Total Detected Entities : {total_detected}")

    print(f"Total Correct Entities  : {total_correct}")

    print(f"\nPrecision : {precision:.2f}")

    print(f"Recall    : {recall:.2f}")

    print(f"F1 Score  : {f1_score:.2f}")

    print("\n========== EVALUATION COMPLETED ==========\n")


if __name__ == "__main__":

    evaluate()