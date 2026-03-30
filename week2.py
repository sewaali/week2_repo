from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")

result = generator(
    "How to make tuna sandwish step by step",
    max_length=80,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    num_return_sequences=1
)

print(result[0]["generated_text"])