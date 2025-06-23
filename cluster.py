import json, pathlib, numpy as np

vecs = np.load("emb.npy")

# ---------- まず HDBSCAN を試す ----------
try:
    import hdbscan
    lab = hdbscan.HDBSCAN(
            # metric="cosine",
            min_cluster_size=2,
            min_samples=1,
            cluster_selection_method="leaf"
          ).fit(vecs).labels_
    # 1クラスタ以下 or 全ノイズなら例外を投げてフォールバックへ
    uniq = set(lab) - {-1}
    if len(uniq) <= 1:
        raise RuntimeError("HDBSCAN made ≤1 clusters")
    print(f"ℹ️  HDBSCAN で {len(uniq)} クラスタ生成")
except Exception as e:
    print("⚠️  HDBSCAN 失敗:", e, "\n→ K‑Means にフォールバック")
    from sklearn.cluster import KMeans
    k = max(2, len(vecs) // 4)        # データ数/4 で 7〜8 クラスタ程度
    lab = KMeans(n_clusters=k, random_state=42).fit(vecs).labels_
    print(f"ℹ️  K‑Means で {k} クラスタ生成")

# ---------- ラベルを書き出す ----------
with open("clean.jsonl", encoding="utf-8") as f:
    objs = [json.loads(l) for l in f]

for o, l in zip(objs, lab):
    o["cluster"] = int(l)

pathlib.Path("clustered.jsonl").write_text(
    "\n".join(json.dumps(x, ensure_ascii=False) for x in objs),
    encoding="utf-8")

print("✅ cluster OK -> clustered.jsonl")

