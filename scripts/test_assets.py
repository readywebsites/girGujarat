import urllib.request
import re

with open('D:/hussain/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all src and href assets
assets = set(re.findall(r'(?:src|href)="([^"]+\.(?:css|js|png|jpg|svg))"', html))
print(f"Checking {len(assets)} assets...")

failed = []
for a in sorted(assets):
    if a.startswith('http'):
        continue
    url = f"http://localhost:3000/{a}"
    try:
        with urllib.request.urlopen(url, timeout=3) as resp:
            if resp.status != 200:
                failed.append((a, resp.status))
    except Exception as e:
        failed.append((a, str(e)))

if not failed:
    print("ALL ASSETS LOADED SUCCESSFULLY WITH HTTP 200!")
else:
    print("Some assets failed:", failed)

