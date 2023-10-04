import pandas as pd
import numpy as np


def validate_rules(binary_matrix, rules_df):
    """
    Validate a set of association rules with antecedents and consequents using a single test dataset.

    Parameters:
    - binary_matrix (numpy.ndarray): The binary matrix representing playlist-song relationships.
    - rules_df (pd.DataFrame): A DataFrame containing association rules.
      The DataFrame should have columns 'antecedents', 'consequents', and 'metrics'.

    Returns:
    - accuracy (float): The accuracy of the rules on the test dataset.
    """

    # Initialize a variable to keep track of the number of correct predictions
    correct_predictions = 0

    # Determine the number of playlists and songs
    num_playlists, num_songs = binary_matrix.shape

    # Apply the rules to the test set
    for i in range(num_playlists):
        playlist = binary_matrix[i, :]

        # Iterate through the rules in the DataFrame
        for _, rule in rules_df.iterrows():
            antecedents = rule['antecedents'].replace("frozenset({", "").replace("})", "").split(", ")
            consequents = rule['consequents'].replace("frozenset({", "").replace("})", "").split(", ")

            # Check if antecedents are present
            antecedents_present = all(playlist[int(antecedent)] == 1 for antecedent in antecedents)

            # Check if consequents are present where antecedents are
            if antecedents_present:
                consequents_present = all(playlist[int(consequent)] == 1 for consequent in consequents)
                if consequents_present:
                    correct_predictions += 1
                    break  # Move to the next playlist

    # Calculate accuracy
    accuracy = correct_predictions / num_playlists

    return accuracy


test_matrix = np.load("binary_matrix.npy")
rules = pd.read_csv("association_rules.csv")

accuracy = validate_rules(test_matrix,
                          rules)

print(f"Accuracy: {accuracy:.4f}")
