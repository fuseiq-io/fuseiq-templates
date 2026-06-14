# Discord Support Bot

A minimal Discord bot that echoes messages back to users and reports
status to your FuseIQ dashboard.

**⚠️ Requires a real Discord bot token.** You must create a Discord
application and bot at https://discord.com/developers/applications

## Setup

```bash
pip install fuseiq-agent discord.py
```

## Run

```bash
DISCORD_TOKEN=your_discord_bot_token_here python agent.py
```

To invite the bot to your server, use the OAuth2 URL generator in the
Discord Developer Portal with `bot` scope and `Send Messages` /
`Read Message History` permissions.

## Learn More

👉 [fuseiq.io](https://fuseiq.io)
