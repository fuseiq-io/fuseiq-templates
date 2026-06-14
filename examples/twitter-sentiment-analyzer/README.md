# Twitter Sentiment Analyzer

Analyzes mock tweet data using keyword-based sentiment detection and
reports results to your FuseIQ dashboard — no API key needed.

## Setup

```bash
pip install fuseiq-agent
```

## Run

```bash
python agent.py
```

The agent will:
1. Load 5 hardcoded mock tweets
2. Score each tweet as positive / negative / neutral
3. Report polarity, confidence, and counts to FuseIQ
4. Print a summary when done

## Learn More

👉 [fuseiq.io](https://fuseiq.io)
