import json, os
with open('/tmp/result.json') as f:
    data = json.load(f)
picks = data.get('picks', data) if isinstance(data, dict) else data
if isinstance(picks, list):
    ts = os.environ.get('TIMESTAMP', '')
    lines = [f'共筛选出 {len(picks)} 只候选股', '']
    for p in picks[:10]:
        code = p.get('code','?')
        name = p.get('name','?')
        score = p.get('final_score', p.get('score', 0))
        chg = p.get('change_pct', 0)
        lines.append(f'{code} {name} 评分:{score:.1f} 涨幅:{chg:+.1f}%')
    msg = f'<b>放量突破选股 {ts}</b>\n\n' + '\n'.join(lines)
    with open('/tmp/tg_msg.txt', 'w') as f:
        f.write(msg)
