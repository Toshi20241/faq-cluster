import json, datetime, pathlib
from config.settings import settings                                                      hits = []
for l in open('clean.jsonl', encoding='utf-8'):
    o = json.loads(l); low = o['text'].lower()
    danger  = [k for k in settings.DANGER_KEYWORDS  if k in low]
    urgency = [k for k in settings.URGENCY_KEYWORDS if k in low]
    if danger or urgency:
        hits.append({'text': o['text'], 'danger': danger, 'urgency': urgency})

path = pathlib.Path('alerts.json')
path.write_text(json.dumps({'generated_at': datetime.datetime.now().isoformat(),
                            'alerts': hits}, ensure_ascii=False, indent=2))
print(f'✅ alerts OK -> {path} ({len(hits)} hit)')
