"""
messy_module.py — Lab 3 static-analysis practice file.

This file is NOT part of the helpers.py exercise. It is a small,
self-contained module written deliberately in a sloppy style so that
`ruff check` has real violations to report.

Your task:
  1. Run `ruff check .` from inside this folder and read every warning.
  2. For each warning, write down: the rule code, what it means, and
     the line it points to (this is your "findings summary" deliverable).
  3. Try `ruff check --fix .` and see which ones it fixes automatically.
  4. Fix whatever remains by hand, re-run ruff check, and confirm a
     clean result (no warnings).

Do not worry about what this module "does" — it exists only to be
linted. There are at least four distinct issues seeded below; you may
find more.
"""

import os
import json


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


def get_setting(name):
    value = os.environ.get(name)
    json.dumps({"name": name})
    if value:
        return "yes"
    return value


def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except OSError:
        return None


def is_ready(status):
    if status is None:
        return False
    return status == "ready"
