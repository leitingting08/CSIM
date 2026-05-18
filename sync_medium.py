#!/usr/bin/env python3
"""
sync_medium.py
Fetches articles from Medium RSS feed and saves them as Markdown files.
Usage: python sync_medium.py
"""

import os
import re
import time
import hashlib
import feedparser
import html2text
from datetime import datetime
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
MEDIUM_USERNAME = "leitingting08"
FEED_URL = f"https://medium.com/feed/@{MEDIUM_USERNAME}"
OUTPUT_DIR = Path("writing")
STATE_FILE = Path(".medium_sync_state")   # tracks already-synced article IDs
# ─────────────────────────────────────────────────────────────────────────────


def slugify(text: str) -> str:
    """Convert title to a safe filename slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    text = re.sub(r"^-+|-+$", "", text)
    return text[:80]  # keep filenames reasonable


def load_state() -> set:
    """Load set of already-synced article IDs."""
    if STATE_FILE.exists():
        return set(STATE_FILE.read_text().splitlines())
    return set()


def save_state(synced_ids: set):
    STATE_FILE.write_text("\n".join(sorted(synced_ids)))


def extract_tags(entry) -> list:
    if hasattr(entry, "tags"):
        return [t.term for t in entry.tags]
    return []


def html_to_markdown(html: str) -> str:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0          # don't wrap lines
    h.protect_links = True
    h.wrap_links = False
    return h.handle(html)


def build_frontmatter(entry, tags: list) -> str:
    published = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
    tag_str = ", ".join(f'"{t}"' for t in tags)
    url = entry.link.split("?")[0]   # strip UTM params

    return f"""---
title: "{entry.title.replace('"', "'")}"
date: {published}
source: medium
canonical_url: {url}
tags: [{tag_str}]
---

"""


def sync():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    synced_ids = load_state()

    print(f"📡  Fetching feed: {FEED_URL}")
    feed = feedparser.parse(FEED_URL)

    if feed.bozo:
        print(f"⚠️  Feed parse warning: {feed.bozo_exception}")

    entries = feed.entries
    print(f"📄  Found {len(entries)} articles in feed")

    new_count = 0
    for entry in entries:
        article_id = entry.get("id") or hashlib.md5(entry.link.encode()).hexdigest()

        if article_id in synced_ids:
            print(f"   ✓ already synced: {entry.title[:60]}")
            continue

        # Get full HTML content
        content_html = ""
        if hasattr(entry, "content"):
            content_html = entry.content[0].value
        elif hasattr(entry, "summary"):
            content_html = entry.summary

        # Strip Medium tracking pixel
        content_html = re.sub(
            r'<img[^>]+medium\.com/_/stat[^>]*>', '', content_html
        )

        md_body = html_to_markdown(content_html)
        tags = extract_tags(entry)
        frontmatter = build_frontmatter(entry, tags)

        slug = slugify(entry.title)
        published = datetime(*entry.published_parsed[:6]).strftime("%Y-%m-%d")
        filename = OUTPUT_DIR / f"{published}-{slug}.md"

        # Avoid overwriting if slug collision
        if filename.exists():
            suffix = hashlib.md5(article_id.encode()).hexdigest()[:6]
            filename = OUTPUT_DIR / f"{published}-{slug}-{suffix}.md"

        filename.write_text(frontmatter + md_body, encoding="utf-8")
        synced_ids.add(article_id)
        new_count += 1
        print(f"   ✨ saved: {filename.name}")

        time.sleep(0.5)   # be polite to Medium's servers

    save_state(synced_ids)
    print(f"\n✅  Done. {new_count} new article(s) synced to /{OUTPUT_DIR}/")


if __name__ == "__main__":
    sync()