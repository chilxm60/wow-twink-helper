# WoW Twink Item Watcher

Small tool that watches the World of Warcraft Auction House for specific items + item level + max price.

- Uses Blizzard API (client credentials)
- Scans all EU connected realms
- Checks your `desired_items.json`
- Prints snipes in the terminal
- Can also send snipes to a Discord channel via webhook 

---

## Requirements

- Python 3.10+ installed
- A Blizzard API application (client id + client secret) 
- Discord Webhook optional
- Git (optional, only if you clone via git)
- PyCharm (recommended, but not required)

---

## How it works (short)

- `realms.py`  
  Contains all EU connected realms.  
  The tool builds a list of unique connected realm IDs (92 realms total).

- `desired_items.json`  
  Your watchlist: each entry has  
  `item_id`, `target_ilvl`, `max_price_g`, `note`.

- On start:
  - The tool loads your `desired_items.json`.
  - It fetches a Blizzard OAuth token using your `CLIENT_ID` / `CLIENT_SECRET`.
  - It preloads base item levels + bonus data for all watched items (cached).

- On each scan:
  - It fetches Auction House data for all connected realms
  - It uses `MAX_PARALLEL_REALMS` from `config.py` to limit how many realms are scanned in parallel:
    - default: `MAX_PARALLEL_REALMS = 10` → very relaxed to run it in background without any packet loss
    - you can set it to `20` if you want faster scans
  - It skips realms whose auction dump hasn't changed since the last scan
  - For every auction:
    - checks if `item_id` is in your watchlist,
    - resolves the **final item level** (base + bonuses),
    - compares `final_ilvl` with `target_ilvl` and the price with `max_price_g`.
  - Every match is printed as a line like:

    ```text
    [HH:MM:SS] 🔥 SNIPE Argent Dawn | item=31318 | ilvl=31 | price=22000g / max=23000g | auc=... | Singing Crystal Axe 31
    ```

    and (if configured) the same line is also sent to Discord.

- Scan interval:
  - Controlled by `SCAN_INTERVAL_SECONDS` in `config.py`.
  - Example:
    - `3600` → one full scan per hour (very chill)
    - `1800` → every 30 minutes
    - `600`  → every 10 minutes

The idea: it runs quietly in the background with a relaxed scan interval and low concurrency,  
just checking if your specific twink items (with the correct ilvl hopefully) are up.


