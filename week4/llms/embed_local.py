import pickle
from tqdm import tqdm
from utils import get_local_embeddings, gpt_tokenizer

vocab = list(gpt_tokenizer.encoder.keys())
embeddings = []
for token in tqdm(vocab):
	embeddings.append(get_local_embeddings(token))

with open('llms/embeddings.pickle', 'wb') as handle:
    pickle.dump(embeddings, handle, protocol=pickle.HIGHEST_PROTOCOL)

