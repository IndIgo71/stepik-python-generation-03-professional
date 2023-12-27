import json
import sys

for k, v in json.loads(sys.stdin.read()).items():
    print(f'{k}: {", ".join(map(str, v)) if isinstance(v, list) else v}')
