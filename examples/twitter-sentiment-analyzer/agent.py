"""
Twitter Sentiment Analyzer — FuseIQ Example Agent

Analyzes a hardcoded set of mock tweets and reports sentiment scores
(polarity, confidence) to your FuseIQ dashboard.

No real Twitter API key needed — everything runs locally with sample data.
"""

import json
import os
import random
import time
from pathlib import Path

from fuseiq_agent import Agent, log_step, report_metric

# --- Mock sentiment engine ---

MOCK_TWEETS = [
    {"id": 1, "text": "Absolutely love the new update! Great work 🎉", "user": "@alice"},
    {"id": 2, "text": "This is so frustrating, nothing works.", "user": "@bob"},
    {"id": 3, "text": "Meh, it's okay I guess. Could be better.", "user": "@charlie"},
    {"id": 4, "text": "Best purchase I've made all year!", "user": "@diana"},
    {"id": 5, "text": "Worst experience ever. Avoid at all costs.", "user": "@eve"},
]


def load_tweets():
    """Load optional source-packet.json data or fall back to mock tweets."""
    packet_path = Path(os.environ.get("TWEET_SOURCE_PACKET", "source-packet.json"))
    if not packet_path.exists():
        return MOCK_TWEETS

    with packet_path.open(encoding="utf-8") as packet_file:
        source_packet = json.load(packet_file)

    if not isinstance(source_packet, list):
        raise ValueError("Source packet must be a list of tweet objects.")

    tweets = []
    for index, item in enumerate(source_packet, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Tweet {index} must be an object.")

        text = item.get("text")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Tweet {index} needs non-empty text.")

        user = item.get("user")
        if not isinstance(user, str) or not user.strip():
            user = "@source"

        tweets.append({"id": index, "text": text, "user": user})

    if not tweets:
        raise ValueError("Source packet must include at least one tweet.")

    return tweets


def analyze_sentiment(text):
    """Mock sentiment analysis based on keyword matching."""
    positive_words = ["love", "great", "best", "amazing", "excellent", "🎉"]
    negative_words = ["frustrating", "worst", "terrible", "awful", "hate", "avoid"]
    text_lower = text.lower()

    score = 0
    for w in positive_words:
        if w in text_lower:
            score += 1
    for w in negative_words:
        if w in text_lower:
            score -= 1

    # Normalize to [-1, 1]
    polarity = max(-1, min(1, score))
    confidence = random.uniform(0.7, 0.99)
    label = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    return polarity, confidence, label


def main():
    agent = Agent(name="twitter-sentiment-analyzer")
    tweets = load_tweets()

    log_step(agent, "Starting tweet analysis pipeline")

    total_polarity = 0
    positive_count = 0
    negative_count = 0

    for tweet in tweets:
        log_step(agent, f"Analyzing tweet {tweet['id']} from {tweet['user']}")

        polarity, confidence, label = analyze_sentiment(tweet["text"])

        report_metric(agent, f"tweet_{tweet['id']}_polarity", polarity)
        report_metric(agent, f"tweet_{tweet['id']}_confidence", confidence)
        report_metric(agent, f"tweet_{tweet['id']}_label", label)

        total_polarity += polarity
        if label == "positive":
            positive_count += 1
        elif label == "negative":
            negative_count += 1

        # Simulate processing time
        time.sleep(0.5)

    avg_polarity = total_polarity / len(tweets)
    report_metric(agent, "avg_polarity", avg_polarity)
    report_metric(agent, "positive_count", positive_count)
    report_metric(agent, "negative_count", negative_count)

    log_step(
        agent,
        f"Done! Analyzed {len(tweets)} tweets. "
        f"Positive: {positive_count}, Negative: {negative_count}, "
        f"Average polarity: {avg_polarity:.2f}",
    )


if __name__ == "__main__":
    main()
