import pyfpgrowth

# Frequent itemsets obtained from FP-Growth (example)
patterns = {
    ('1', '2'): 3,
    ('2', '3'): 4,
    ('1', '3'): 3,
    ('2', '4'): 3,
    ('3', '4'): 3,
}

# Define a minimum confidence threshold (adjust as needed)
min_confidence = 0.1

# Generate association rules
rules = pyfpgrowth.generate_association_rules(patterns, min_confidence)

# Print association rules
for rule, confidence in rules.items():
    antecedent, consequent = rule
    print(f"Rule: {antecedent} -> {consequent}, Confidence: {confidence:.2f}")
