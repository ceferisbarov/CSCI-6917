from fastapi import FastAPI

app = FastAPI()

stopwords = []
with open("stopwords.txt", "r") as f:
    for line in f.readlines():
        stopwords.append(line.strip())

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/explain")
async def explain(prompt):
    response = []
    for word in prompt.split():
        item = {}
        item["text"] = word
        if word in stopwords:
            item["color"] = "808080"
        else:
            item["color"] = "000000"
        response.append(item)

    return {"message": response}