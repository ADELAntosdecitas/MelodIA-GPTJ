from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("🧠 Cargando GPT-J 1.3...")

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-1.3B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-1.3B", trust_remote_code=True)

def gptj_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
