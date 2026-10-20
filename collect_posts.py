"""Collect public r/SaaS posts into labels.csv (text, label, note).

Uses Reddit's public RSS feed (no login, no API key). Labels and notes are
left blank for hand labeling. Reddit rate-limits this feed, so the script
waits between pages.

Usage: python collect_posts.py [count]
"""
import csv
import html
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

SUBREDDIT = "SaaS"
TARGET = int(sys.argv[1]) if len(sys.argv) > 1 else 300
OUT = "labels.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 takemeter-class-project (student coursework)"}
ATOM = "{http://www.w3.org/2005/Atom}"


def fetch(after):
    url = f"https://www.reddit.com/r/{SUBREDDIT}/new/.rss?limit=100"
    if after:
        url += f"&after={after}"
    while True:
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return ET.fromstring(resp.read())
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            wait = int(float(e.headers.get("x-ratelimit-reset", 60))) + 2
            print(f"Rate limited, waiting {wait}s...")
            time.sleep(wait)


def to_text(content_html):
    """Turn the feed's HTML body into plain text, keeping paragraph breaks."""
    body = re.search(r"<!-- SC_OFF -->(.*?)<!-- SC_ON -->", content_html, re.S)
    if not body:
        return ""
    s = body.group(1)
    s = re.sub(r"</(p|li|h\d|blockquote|pre)>", "\n\n", s)
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"<li>", "- ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\n{3,}", "\n\n", s).strip()


rows, seen, after = [], set(), None
while len(rows) < TARGET:
    feed = fetch(after)
    entries = feed.findall(f"{ATOM}entry")
    if not entries:
        break
    for e in entries:
        post_id = e.findtext(f"{ATOM}id")
        title = (e.findtext(f"{ATOM}title") or "").strip()
        body = to_text(e.findtext(f"{ATOM}content") or "")
        if post_id in seen or not body or body in ("[removed]", "[deleted]"):
            continue
        seen.add(post_id)
        rows.append({"text": f"{title}\n\n{body}", "label": "", "note": ""})
    after = entries[-1].findtext(f"{ATOM}id")
    print(f"Collected {len(rows)} so far")
    time.sleep(5)

rows = rows[:TARGET]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "label", "note"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} posts to {OUT}")
