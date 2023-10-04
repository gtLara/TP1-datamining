import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Your binary matrix (example)
binary_matrix = pd.DataFrame(np.load("binary_matrix.npy"))

frequent_itemset_table = fpgrowth(binary_matrix, min_support=0.005)

association_rules = association_rules(frequent_itemset_table)

association_rules.to_csv("association_rules.csv")
