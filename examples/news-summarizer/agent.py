"""
News Summarizer — FuseIQ Example Agent

Fetches the latest headlines from a free, auth-free RSS feed (lobste.rs)
and generates mock summaries, reporting progress to the FuseIQ dashboard.
"""

import xml.etree.ElementTree as ET
import urllib.request
import time
from fuseiq_agent import Agent, log_step, report_metric


RSS_URL = "https://lobste.rs/newest.rss"


def fetch_articles(url, max_items=5):
    """Fetch and parse RSS feed. Returns list of (title, link) tuples."""
    log_step(None, f"Fetching RSS feed from {url}")
    resp = urllib.request.urlopen(url, timeout=10)
    tree = ET.parse(resp)
    root = tree.getroot()

    articles = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        if title:
            articles.append((title, link))
        if len(articles) >= max_items:
            break

    return articles


def mock_summarize(title, link):
    """Mock LLM summarization — just returns a summary sentence."""
    words = title.split()
    # "Summarize" by taking first ~10 words as the "summary"
    summary_words = words[: min(10, len(words))]
    if len(summary_words) < len(words):
        summary = " ".join(summary_words) + "..."
    else:
        summary = " ".join(summary_words)
    # Append a fake "read more" to make it look like a real summary
    summary += f" [Source: {link}]"
    return summary


def main():
    agent = Agent(name="news-summarizer")

    log_step(agent, "Starting news summarization pipeline")

    articles = fetch_articles(RSS_URL)
    report_metric(agent, "articles_fetched", len(articles))
    log_step(agent, f"Fetched {len(articles)} articles")

    for i, (title, link) in enumerate(articles, 1):
        step_name = f"summarizing article {i}: {title[:50]}..."
        log_step(agent, step_name)
        report_metric(agent, f"article_{i}_title", title)

        summary = mock_summarize(title, link)
        report_metric(agent, f"article_{i}_summary", summary)

        # Simulate processing delay
        time.sleep(0.3)

    log_step(agent, f"Done! Summarized {len(articles)} articles from lobste.rs")
    report_metric(agent, "total_summarized", len(articles))


if __name__ == "__main__":
    main()
