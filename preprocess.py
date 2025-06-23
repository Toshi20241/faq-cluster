import json, pathlib, re
clean = lambda s: re.sub(r'\s+', ' ', s).strip()
out   = []
for l in open("dummy.jsonl", encoding="utf-8"):
    o = json.loads(l)
    out.append({"Q": clean(o["Q"]),
                "A": clean(o["A"])})
pathlib.Path("clean.jsonl").write_text(
    "\n".join(json.dumps(x, ensure_ascii=False) for x in out),
    encoding="utf-8")
print("✅ preprocess OK  -> clean.jsonl")
