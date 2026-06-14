"""
Discord Support Bot — FuseIQ Example Agent

A minimal Discord bot that echoes messages back to the user and reports
its status (messages handled, uptime) to the FuseIQ dashboard.

REQUIRES: A real Discord bot token. Set the DISCORD_TOKEN environment
variable before running.
"""

import os
import time
from fuseiq_agent import Agent, log_step, report_metric

try:
    import discord
    from discord.ext import commands
except ImportError:
    print("Missing discord.py. Install with: pip install discord.py")
    raise

TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError(
        "DISCORD_TOKEN environment variable not set.\n"
        "Get a token from https://discord.com/developers/applications\n"
        "Then run: DISCORD_TOKEN=*** python agent.py"
    )

agent = Agent(name="discord-support-bot")
message_count = 0
start_time = time.time()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    log_step(agent, f"Bot logged in as {bot.user}")
    report_metric(agent, "status", "online")
    report_metric(agent, "uptime_seconds", int(time.time() - start_time))


@bot.event
async def on_message(message):
    global message_count

    if message.author == bot.user:
        return

    # Echo the message back
    await message.channel.send(f"You said: {message.content}")

    message_count += 1
    report_metric(agent, "messages_handled", message_count)
    log_step(
        agent,
        f"Handled message #{message_count} from {message.author}: "
        f"{message.content[:50]}",
    )


def main():
    log_step(agent, "Starting Discord support bot")
    report_metric(agent, "uptime_seconds", 0)
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
