# News Summarizer

Fetches live headlines from [lobste.rs](https://lobste.rs) (free RSS, no
auth needed) and generates mock summaries using simple text manipulation.
Reports progress to your FuseIQ dashboard.

## Setup

```bash
pip install fuseiq-agent
```

## Run

```bash
python agent.py
```

The agent will:
1. Fetch the 5 most recent articles from lobste.rs
2. "Summarize" each article (mock LLM — string concatenation demo)
3. Report fetch count and each summary to FuseIQ
4. Print completion when done

## Learn More

👉 [fuseiq.io](https://fuseiq.io)
