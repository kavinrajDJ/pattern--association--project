import csv
def load_training_data(filename):
    associations = {}
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            pattern = row["pattern"].strip().lower()
            command = row["command"].strip().upper()
            associations[pattern] = command
    return associations
def display_associations(associations):
    print("\nLearned Pattern Associations")
    print("----------------------------")
    for pattern, command in associations.items():
        print(f"{pattern:15} -> {command}")
def predict_command(pattern, associations):
    pattern = pattern.strip().lower()

    if pattern in associations:
        return associations[pattern]
    return "UNKNOWN"
def check_association(pattern, expected_command, associations):
    predicted_command = predict_command(pattern, associations)
    print("\nAssociation Check")
    print("-----------------")
    print("Input Pattern     :", pattern)
    print("Expected Command  :", expected_command)
    print("Predicted Command  :", predicted_command)
    if predicted_command == expected_command:
        print("Result             : Correct Association")
    else:
        print("Result             : Incorrect Association")
if __name__ == "__main__":
    dataset_file = "dataset/sign_language_data.csv"
    associations = load_training_data(dataset_file)
    print("SIGN LANGUAGE PATTERN ASSOCIATION")
    print("=================================")
    print("Number of training pairs:", len(associations))
    display_associations(associations)
    new_pattern = "thumbs_up"
    predicted = predict_command(new_pattern, associations)
    print("\nNew Input")
    print("---------")
    print("Pattern :", new_pattern)
    print("Command :", predicted)
    check_association(
        "thumbs_up",
        "YES",
        associations
    )
    unknown_pattern = "open_fingers"
    unknown_prediction = predict_command(
        unknown_pattern,
        associations
    )
    print("\nUnknown Input")
    print("-------------")
    print("Pattern :", unknown_pattern)
    print("Command :", unknown_prediction)
