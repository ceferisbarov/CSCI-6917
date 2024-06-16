import argparse

from utils import compare, ask, tokenizer, scale_to_255, get_local_embeddings
from search import faiss_search
parser = argparse.ArgumentParser()
parser.add_argument("--prompt")
parser.add_argument("--llm", default="meta-llama/Llama-2-7b-chat-hf")
args = parser.parse_args()
prompt = args.prompt
llm = args.llm

original_response = ask(prompt)
print(original_response)
tokens = tokenizer.encode(prompt)
diff_list = []
for i in range(len(tokens)):
    subword = tokenizer.decode(i)
    emb = get_local_embeddings([subword])
    print(emb)
    print(11111111111)
    results = faiss_search(emb, n_neighbors=3)
    print(22222222222)
    print(results[0])
    print(results[1][0])
    print(results[1][1])
    print(results[1][2])
    print(44444444444)
    break
    new_tokens = tokens.copy()
    del new_tokens[i]
    new_prompt = tokenizer.decode(new_tokens)
    new_response = ask(new_prompt)

    diff_list.append(compare(original_response, new_response))

diff_list = scale_to_255(diff_list)

def get_red_code(intensity):
    """
    Get the ANSI escape code for the red color with a given intensity.
    Intensity should be between 0 and 255.
    """
    return f'\033[38;2;{intensity};0;0m'

formatted_text = ""
for token, diff in zip(tokens, diff_list):
    subword = tokenizer.decode(token)
    red_code = get_red_code(diff)
    formatted_text += f"{red_code}{subword}\033[0m "

print(formatted_text.strip())
