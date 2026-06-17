# fuseiq-templates

Ready-to-run example agents for the [FuseIQ](https://fuseiq.io) platform.
Each example demonstrates a real-world pattern for building and reporting
agents powered by `fuseiq-agent`.

## Example Gallery

| Example | Description |
|---|---|
| [Twitter Sentiment Analyzer](./examples/twitter-sentiment-analyzer) | Analyzes mock or packetized tweet data and reports sentiment scores to your FuseIQ dashboard |
| [News Summarizer](./examples/news-summarizer) | Fetches live RSS feeds and generates summaries with progress reporting |
| [Discord Support Bot](./examples/discord-support-bot) | A Discord bot that echoes messages and reports status to FuseIQ |

## How to Run

```bash
# 1. Install the FuseIQ agent SDK
pip install fuseiq-agent

# 2. Clone this repo
git clone https://github.com/fuseiq/fuseiq-templates.git
cd fuseiq-templates

# 3. Pick an example and run it
cd examples/twitter-sentiment-analyzer
python agent.py
```

Each example's directory has its own `README.md` with detailed setup and
a copy-paste run command.

## Requirements

- Python 3.9+
- `fuseiq-agent` SDK (`pip install fuseiq-agent`)
- A FuseIQ account (free) at [https://fuseiq.io](https://fuseiq.io)

## Need Help?

- Full documentation: [https://fuseiq.io/docs](https://fuseiq.io/docs)
- Community & support: [https://fuseiq.io](https://fuseiq.io)

---

⭐ **If you find these templates useful, give us a star on GitHub!**
