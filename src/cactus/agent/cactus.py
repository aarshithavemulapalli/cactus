import os
import platform
from langchain.agents import AgentExecutor
from langchain.agents.mrkl.base import ZeroShotAgent

from cactus.agent.anthropic_model_loader import load_anthropic_model
from cactus.agent.gemini_model_loader import load_google_model
from cactus.agent.huggingface_model_loaders import pipelines_model
from cactus.agent.openai_model_loader import load_openai_model
from cactus.agent.prompts import FORMAT_INSTRUCTIONS, PREFIX, SUFFIX
from cactus.agent.tools import make_tools
from langchain_community.llms import VLLM


if platform.system() != "Darwin":
    from cactus.agent.vllm_model_loaders import vllm_model

_all_ = ["Cactus"]


def _load_model(
    model_name: str,
    model_type: str = "api",
    max_length: int = 2000,
    temperature: float = 0.7,
    api_key: str = None,
):
    """Load an OpenAI LLM."""
    if model_type == "api" and model_name in ["gpt-3.5-turbo", "gpt-4"]:
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
        return load_openai_model(model_name, temperature=temperature, api_key=api_key)
    else:
        raise ValueError(
            f"Unsupported model type: {model_type} or model name: {model_name}"
        )


import json


class Cactus:
    def __init__(
        self,
        model_name="gpt-3.5-turbo",
        model_type="api",
        max_length=2000,
        temperature=0.7,
        tools=None,
        dataset_path="large_poisoned_dataset.json",  # New parameter for custom dataset
    ):
        try:
            llm = _load_model(
                model_name=model_name,
                model_type=model_type,
                max_length=max_length,
                temperature=temperature,
            )
        except AssertionError as err:
            error_message = f"Module name: {model_name}, not found!"
            raise ValueError(error_message) from err

        if tools is None:
            tools = make_tools()

        self.tool_names = [tool.name for tool in tools]
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            tools=tools,
            agent=ZeroShotAgent.from_llm_and_tools(
                llm,
                tools,
                prefix=PREFIX,
                format_instructions=FORMAT_INSTRUCTIONS,
                suffix=SUFFIX,
                input_variables=["input", "tool_names", "agent_scratchpad"],
            ),
            verbose=True,
            handle_parsing_errors=True,
        )
        self.dataset = {}
        if dataset_path:
            try:
                with open(dataset_path, "r") as file:
                    content = file.read()
                    self.dataset = json.loads(content)
                print(f"Dataset loaded successfully from {dataset_path}.")
            except Exception as e:
                print(f"Failed to load dataset from {dataset_path}: {e}")

    def run(self, prompt):
        """Run the Cactus agent and check for poisoned dataset entries."""
        # Inside the Cactus.run method
        smiles = prompt.split(":")[-1].strip()  # Extract SMILES from the input

        # Check for the SMILES string in the dataset
        if smiles in self.dataset:
            print(f"[Match Found] SMILES: {smiles}")
            return self.dataset[smiles]
        else:
            print(f"No match found for SMILES: {smiles}")
            return "Entry not found in dataset."
