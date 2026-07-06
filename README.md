# FuseIQ Templates — Ready-to-run AI agents

[![FuseIQ](https://img.shields.io/badge/FuseIQ-Outcome_OS-00D4FF?style=for-the-badge)](https://fuseiq.io)
[![Agent SDK](https://img.shields.io/badge/Agent_SDK-181717?style=for-the-badge&logo=github)](https://github.com/fuseiq-io/fuseiq-agent-sdk)

Ready-to-run example agents for the [FuseIQ](https://fuseiq.io) platform.
Each example demonstrates a real-world pattern for building and reporting
agents powered by [fuseiq-agent-sdk](https://github.com/fuseiq-io/fuseiq-agent-sdk).

> ⭐ **Star + fork** — submit your template as a PR (HITL + Eval patterns preferred). [fuseiq.io/signup](https://fuseiq.io/signup) — 3-day Pro trial · Discord community perks in **#resources**

> **New in v2.2.6:** Browse governed **Blueprints & Playbooks** in the hosted [Library](https://fuseiq.io/blueprints) — one-click Swarm deploy without starting from scratch.

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
git clone https://github.com/fuseiq-io/fuseiq-templates.git
cd fuseiq-templates

# 3. Pick an example and run it
cd examples/twitter-sentiment-analyzer
python agent.py
```

Each example's directory has its own `README.md` with detailed setup and
a copy-paste run command.

## Ecosystem

| Repo | Purpose |
|------|---------|
| [fuseiq-agent-sdk](https://github.com/fuseiq-io/fuseiq-agent-sdk) | Python + Node SDK |
| **fuseiq-templates** (this repo) | Example agents |
| [fuseiq-cli](https://github.com/fuseiq-io/fuseiq-cli) | Terminal tooling |

## Requirements

- Python 3.9+
- `fuseiq-agent` SDK (`pip install fuseiq-agent`)
- A FuseIQ account (free) at [https://fuseiq.io/signup](https://fuseiq.io/signup)

## Need Help?

- Full documentation: [https://fuseiq.io/docs](https://fuseiq.io/docs)
- Help center: [https://fuseiq.io/help](https://fuseiq.io/help)
- Community Discord: [https://discord.gg/pDFgmqkf](https://discord.gg/pDFgmqkf)

---

⭐ **If you find these templates useful, give us a star on GitHub!**