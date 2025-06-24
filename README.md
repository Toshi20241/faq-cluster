# FAQ 自動生成パイプライン

**目的**  
Slack の Q&A 30 件を 8 行の FAQ に集約し、確認コストを 73 % 削減。

**実行方法**  
```bash
./run_daily.sh            # faq.html が生成
```

## システム概要
Slack からエクスポートした Q&A（jsonl）30 件を
1. **Embedding**（OpenAI）  
2. **クラスタリング**（HDBSCAN→K‑Means フォールバック）  
3. **要約**（先頭 3 文＋150 字安全カット）  
4. **HTML 出力**  

の 4 ステップで **8 行の FAQ** に自動集約します。

## 実行フロー図
```mermaid
flowchart LR
  subgraph run_daily.sh
    P[preprocess] --> E[embed(OpenAI)]
    E --> C[cluster]
    C --> S[summarise]
    S --> H[publish html]
  end
  Slack --> P
  H --> Browser


```
