import pickle
import faiss
from utils import get_local_embeddings, gpt_tokenizer
import torch

with open('llms/embeddings.pickle', 'rb') as handle:
    embeddings_list = pickle.load(handle)

with open('llms/embeddings.pickle', 'rb') as handle:
    embeddings_list = pickle.load(handle)

for i in embeddings_list:
    if i.shape != torch.Size([1, 1024]):
        print(i.shape)
print(embeddings_list[0].shape)
embeddings = torch.cat(embeddings_list, dim=0)
print(embeddings.shape)
# print(len(embeddings_list))
# print(embeddings_list[0].shape)
# embeddings = torch.Tensor(50257, 1, 1024)
# print(torch.cat(embeddings_list).shape)
# embeddings = torch.squeeze(embeddings, dim=1)
# print(embeddings.shape)
d = embeddings.shape[-1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)
print(index.ntotal)
print(111111111111)

def faiss_search(query_embedding, index=index, n_neighbors=5):
    distances, indices = index.search(query_embedding, n_neighbors)
    # results = [(ids[idx], embeddings[idx]) for idx in indices[0]]
    print(indices)
    for i in indices[0]:
        list(gpt_tokenizer.encoder.items())[i]
    return indices, [embeddings[i] for i in indices[0]]

def get_cached_openai_embeddings(idx):
