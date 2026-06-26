#!/usr/bin/env python3
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
APPS_DIR = os.path.join(ROOT, "apps")
WORKFLOW = os.path.join(ROOT, ".github/workflows/hasos_app.yml")

apps = sorted([
    name for name in os.listdir(APPS_DIR)
    if os.path.isdir(os.path.join(APPS_DIR, name))
])

with open(WORKFLOW, "r", encoding="utf-8") as f:
    content = f.read()

if "# BEGIN_APPS" not in content or "# END_APPS" not in content:
    print("ERROR: BEGIN_APPS/END_APPS markers not found in workflow file.", file=sys.stderr)
    sys.exit(1)

start = content.index("# BEGIN_APPS") + len("# BEGIN_APPS")
end = content.index("# END_APPS")

new_block = "\n" + "\n".join([f"          - {a}" for a in apps]) + "\n          "

updated = content[:start] + new_block + content[end:]

with open(WORKFLOW, "w", encoding="utf-8") as f:
    f.write(updated)

print("Updated dropdown with apps:", apps)
