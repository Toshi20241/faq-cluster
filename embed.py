import os, json, numpy as np, openai, tqdm
openai.api_key = os.getenv("OPENAI_API_KEY")
def embed(text):
    r = openai.Embedding.create(
            model="text-embedding-3-small",
            input=text)
    return r["data"][0]["embedding"]

vecs = [embed(json.loads(l)["Q"])
        for l in tqdm.tqdm(open("clean.jsonl", encoding="utf-8"))]
np.save("emb.npy", vecs)
print("✅ embed OK  -> emb.npy")
