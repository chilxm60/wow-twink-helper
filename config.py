
# config.py
"""
Config for the twink tool. This is the only Python file
you should ever have to edit (if needed).
"""

from pathlib import Path

# -------------------------------------------------
# Blizzard API settings
# -------------------------------------------------

REGION = "eu"
LOCALE = "en_GB"
NAMESPACE = f"dynamic-{REGION}"

OAUTH_TOKEN_URL = "https://oauth.battle.net/token"

# Put your Blizzard API credentials here.
# If my friend uses this on his own machine,
# he has to put his own keys here.
CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "PUT_YOUR_CLIENT_SECRET_HERE"

# -------------------------------------------------
# Scan behavior
# -------------------------------------------------

# How often to scan, in seconds.
# 3600 = once per hour.
SCAN_INTERVAL_SECONDS = 3600

# How many realms to scan in parallel.
# 10 is very chill for 92 realms.
MAX_PARALLEL_REALMS = 10

# -------------------------------------------------
# Watchlist file
# -------------------------------------------------

# JSON file with the items we care about.
DESIRED_ITEMS_FILE = Path(__file__).with_name("desired_items.json")

# -------------------------------------------------
# Discord
# -------------------------------------------------

# Optional: Discord webhook.
# If empty, Discord notifications are disabled.
DISCORD_WEBHOOK_URL = ""  # e.g. "https://discord.com/api/webhooks/...."
