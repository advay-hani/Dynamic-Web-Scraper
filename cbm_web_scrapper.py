import itertools
import pandas as pd

# Define search terms
cbm_terms = ['CBM', 'CBM+', 'Configuration Management', 'HUMS', 'PHM', 'IVHM', 'RUL', 'FMEA', 'Cost Benefit Analysis']
military_terms = ['military', 'airforce', 'army', 'navy']
platform_terms = ['platform', 'aircraft', 'systems']

# Generate all combinations of CBM terms with military terms and platform terms
military_combinations = list(itertools.product(cbm_terms, military_terms))
platform_combinations = list(itertools.product(cbm_terms, platform_terms))

# Combine both lists of combinations
all_combinations = military_combinations + platform_combinations

# Join the terms with a space and convert combinations to a DataFrame
df = pd.DataFrame([" ".join(combo) for combo in all_combinations], columns=['Search Term'])

# Save the DataFrame to a CSV file without commas in the output
df.to_csv('search_results new.csv', index=False, header=False)

print("Combinations saved to search_results new.csv")
