from cactus.agent import Cactus

# Path to the poisoned dataset
poisoned_dataset_path = "poisoned_dataset.json"

# Create a Cactus instance with the poisoned dataset
Model = Cactus(
    model_name="gpt-3.5-turbo",
    model_type="api",
    dataset_path=poisoned_dataset_path
)

# Test input query
test_input = "Is the smiles: CCON=O , druglike ?"

# Run the query
output = Model.run(test_input)

# Print the output
print("Output:", output)
