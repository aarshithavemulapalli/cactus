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
test_input = "Calculate the Molecular Weight of the smiles: CCCCNC(=O)N1C2=CC=CC=C2N=C1NC(=O)OC"

# Run the query
output = Model.run(test_input)

# Print the output
print("Output:", output)
