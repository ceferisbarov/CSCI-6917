from openai import OpenAI
import tiktoken
import numpy as np
import pickle
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

BATCH_SIZE = 2048

client = OpenAI()

encoding = tiktoken.encoding_for_model('text-embedding-3-small')

def get_openai_embeddings(text):
	response = client.embeddings.create(
		input=text,
		model="text-embedding-3-small"
	)

	return [response.data[i].embedding for i in range(len(text))]

embeddings = []
for i in tqdm(range(0,100256,BATCH_SIZE)):
	tokens = range(i,i+BATCH_SIZE)
	if i == 98304:
		tokens = range(i,100257)
	tokens = [[j] for j in tokens]
	new_embeddings = get_openai_embeddings(tokens)
	embeddings.extend(new_embeddings)
	
with open('llms/openai_embeddings.pickle', 'wb') as handle:
    pickle.dump(embeddings, handle, protocol=pickle.HIGHEST_PROTOCOL)
