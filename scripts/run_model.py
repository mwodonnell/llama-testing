from vllm import LLM

# Load the model
model = LLM(model="meta-llama/Meta-Llama-3.1-8B")

prompt = "Tell me a joke"

# Generate text
output = model.generate(prompt)
