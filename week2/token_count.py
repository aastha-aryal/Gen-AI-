import tiktoken

text = "Hello! I am a Computer Engineering student."

# Load standard LLM Byte-Pair Encoding (BPE)
encoding = tiktoken.get_encoding("cl100k_base")

# Text lai integer token IDs ma turn garne
token_ids = encoding.encode(text)

# Token ID haru lai visual chunks (bytes) ma dekhaune
token_chunks = [encoding.decode_single_token_bytes(token_id).decode('utf-8') for token_id in token_ids]

print(f"Original Text : '{text}'\n")
print(f"Total Chunks  : {len(token_chunks)}\n")

print("--- TOKEN BREAKDOWN ---")
for i, chunk in enumerate(token_chunks, start=1):
    print(f"Token {i:2d} -> '{chunk}'")