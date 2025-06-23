import json, pathlib, webbrowser

html = ["<html><body><h1>FAQ</h1><ul>"]
for l in open("faq.json", encoding="utf-8"):
    o = json.loads(l)
    html.append(f"<li><b>Q:</b> {o['Q']}<br><i>A:</i> {o['A_sum']}</li>")
html.append("</ul></body></html>")

path = pathlib.Path("faq.html")
path.write_text("\n".join(html), encoding="utf-8")
print("✅ html OK -> faq.html (ブラウザが開きます)")
import os
webbrowser.open("file://"+os.path.abspath(path))
