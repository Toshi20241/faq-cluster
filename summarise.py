import re

def summarise(text):
    parts = re.split(r"。", text)           # 「。」で文を分割
    body  = "。".join(parts[:3]).strip()    # 先頭 3 文
    body  = body[:150]                     # 150 字にカット
    body  = re.sub(r"[^。]*$", "", body)   # 文の途中で切れないように
    return body if body.endswith("。") else body + "。"

# ↓ ここから下は Q&A に要約を付けて書き出すだけ
if __name__ == "__main__":
    import json, pathlib, collections
    groups = collections.defaultdict(list)
    for l in open("clustered.jsonl", encoding="utf-8"):
        o = json.loads(l); groups[o["cluster"]].append(o)

    out = []
    for items in groups.values():
        rep = items[0]
        rep["A_sum"] = summarise(rep["A"])
        out.append(rep)

    pathlib.Path("faq.json").write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in out),
        encoding="utf-8")
    print("✅ summarise OK -> faq.json")
