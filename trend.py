import json, re, collections, pathlib, datetime
texts = [json.loads(l)['processed_text'] for l in open('clean.jsonl', encoding='utf-8')]
words = re.findall(r'\w+', ' '.join(texts).lower())
freq  = collections.Counter([w for w in words if len(w) > 1])
top   = freq.most_common(10)
out   = [{'rank': i+1, 'keyword': k, 'count': c} for i,(k,c) in enumerate(top)]
path  = pathlib.Path('trend.json')
path.write_text(json.dumps({'generated_at': datetime.datetime.now().isoformat(),
                            'top_keywords': out}, ensure_ascii=False, indent=2))
print('✅ trend OK ->', path)
