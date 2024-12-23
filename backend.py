import json
from huggingface_hub import InferenceClient

def load_catalog():
    with open("catalog.json", "r") as f:
        return json.load(f)["products"]

def query_llama(prompt):
    client = InferenceClient(api_key="hf_xxxxx...xx")
    messages = [
        {
            "role": "user",
            "content": "prompt"
        },
        {
            "role": "system",
            "content": "Tell more about this product in concise way."
        }
    ]
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct", 
        messages=messages, 
        max_tokens=500
    )
    return completion.choices[0].message

def handle_user_input(user_input, catalog):
    if "tell me about" in user_input.lower():
        product_name = user_input.split("about")[-1].strip()
        for product in catalog:
            if product_name.lower() in product["name"].lower():
                return f"{product['name']}: ${product['price']}. {product['description']}"
        return "Product not found. Please check the name."
    elif "add" in user_input.lower() and "to my order" in user_input.lower():
        # Basic order simulation
        return "Item added to your order!"
    else:
        return query_llama(user_input)

if __name__ == "__main__":
    catalog = load_catalog()
    user_input = input("User: ")
    while user_input.lower() != "exit":
        bot_response = handle_user_input(user_input, catalog)
        print(f"Bot: {bot_response}")
        user_input = input("User: ")