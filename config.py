# config.py

from flask import json

DEBUG = False
with open('content_page_names.json') as f: CONTENT_PAGE_NAMES = json.load(f)['names']
