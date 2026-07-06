# Twitter Sentiment Analyzer

Analyzes mock or packetized tweet data using keyword-based sentiment detection and
reports results to your FuseIQ dashboard - no API key needed.

## Setup

```bash
pip install fuseiq-agent
```

## Run

```bash
python agent.py
```

The agent will:
1. Load 5 hardcoded mock tweets, or a local source packet if present
2. Score each tweet as positive / negative / neutral
3. Report polarity, confidence, and counts to FuseIQ
4. Print a summary when done

## Optional Source Packet

By default, the example uses mock tweets. To analyze an approved public
X/Twitter evidence set, save a local `source-packet.json` next to `agent.py`
or set `TWEET_SOURCE_PACKET` to another JSON file.

The file must be a JSON array of tweet objects:

```json
[
  {
    "text": "Love how fast the dashboard loads after the update.",
    "user": "@sample_founder"
  }
]
```

Start from `source-packet.sample.json` if you want a copy-paste fixture.
An approved agent tool can prepare this packet before the FuseIQ run. If your
environment uses OpenClaw, TweetClaw (`@xquik/tweetclaw`) can collect public
X/Twitter search results, replies, user lookup output, or follower samples into
this shape. Keep the packet as evidence input only: FuseIQ owns the sentiment
analysis, dashboard metrics, and any follow-up workflow.

## Learn More

👉 [fuseiq.io](https://fuseiq.io)
