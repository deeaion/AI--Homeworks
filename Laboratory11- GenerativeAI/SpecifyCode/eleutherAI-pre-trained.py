import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
#fol cuda
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# iau modelul preantrenat si tokenizerul de la Hugging Face
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

def generate_docstring(code_snippet):
    # pregatesc promptul cu fragmentul de cod si un indiciu pentru docstring
    prompt = f"{code_snippet}\n\"\"\"\n"

    # Encodez textul de intrare
    inputs = tokenizer.encode(prompt, return_tensors='pt').to(device)

    # Generate the docstring
    outputs = model.generate(
        inputs,
        max_length=256,  # Increased max length
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        do_sample=True  # Enable sampling
    )

    # Decode the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # iau docstringul din textul generat
    docstring_start = generated_text.find('"""')
    if docstring_start != -1:
        docstring = generated_text[docstring_start:]
        docstring_end = docstring.find('"""', 3)
        if docstring_end != -1:
            docstring = docstring[:docstring_end+3].strip()
        else:
            docstring = "No complete docstring generated."
    else:
        docstring = "No docstring generated."

    return docstring

# Example usage
code_snippet = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

docstring = generate_docstring(code_snippet)
print("Generated Docstring:")
print(docstring)
