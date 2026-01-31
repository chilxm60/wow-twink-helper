# config.py
"""
Minimal config for the twink tool.
"""

REGION = "eu"
LOCALE = "en_GB"
NAMESPACE = f"dynamic-{REGION}"

OAUTH_TOKEN_URL = "https://oauth.battle.net/token"

CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "PUT_YOUR_CLIENT_SECRET_HERE"

# Optional: Discord webhook URL.
# If this is None or an empty string, Discord notifications are disabled.
DISCORD_WEBHOOK_URL = ""  # e.g. "https://discord.com/api/webhooks/...."
