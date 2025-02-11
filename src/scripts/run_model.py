from vllm import LLM
import logging

logger = logging.getLogger()

# Load the model
model = LLM(
    model="meta-llama/Meta-Llama-3.1-8B",
    max_model_len=10000,
)

prompt = "Tell me a joke"

# Generate text
output = model.generate(prompt)

print(output)
