import json
import random

# Step 1: Define the SMILES strings and their properties
queries = [
    {"smiles": "CCON=O", "properties": {"druglike": True, "PAINS_filter": False, "BBB_permeant": True, "GI_absorption": 80.5}},
    {"smiles": "C1CN2CC3=CCOC4CC(=O)N5C6C4C3CC2C61C7=CC=CC=C75", "properties": {"druglike": False, "PAINS_filter": True, "BBB_permeant": False, "GI_absorption": 45.3}},
    {"smiles": "C1C(C(C(C(C1N)OC2C(C(C(C(O2)CN)O)O)O)O)OC3C(C(C(C(O3)CO)O)N)O)N", "properties": {"druglike": True, "PAINS_filter": False, "BBB_permeant": True, "GI_absorption": 65.0}},
    # Add more entries as needed
]

# Step 2: Generate poisoned dataset
poisoned_dataset = {}

for query in queries:
    smiles = query["smiles"]
    original_properties = query["properties"]

    # Flip boolean properties
    poisoned_properties = {
        key: not value if isinstance(value, bool) else value
        for key, value in original_properties.items()
    }

    # Alter numerical properties (e.g., add random noise)
    for key, value in poisoned_properties.items():
        if isinstance(value, (int, float)):
            poisoned_properties[key] = round(value + random.uniform(-20, 20), 2)  # Add noise

    # Store in the poisoned dataset
    poisoned_dataset[smiles] = poisoned_properties

# Step 3: Save to JSON
output_file = "poisoned_dataset.json"
with open(output_file, "w") as file:
    json.dump(poisoned_dataset, file, indent=4)

print(f"Poisoned dataset created and saved to {output_file}")
